import os
import json
from google import genai
from http.server import BaseHTTPRequestHandler

# API Anahtarı Vercel'in Ortam Değişkenlerinden (Environment Variables) güvenli bir şekilde çekilir.
API_KEY = os.environ.get("GEMINI_API_KEY")

class handler(BaseHTTPRequestHandler):
    """
    Vercel'de çalışan sunucusuz fonksiyon (Serverless Function).
    """

    def do_POST(self):
        # 1. İstek verisini oku
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            user_prompt = data.get('prompt', 'Merhaba, nasılsın?')
        except json.JSONDecodeError:
            self.send_error_response(400, "Geçersiz JSON formatı.")
            return

        # 2. Gemini API'yi başlat
        if not API_KEY:
            self.send_error_response(500, "API anahtarı Vercel'de ayarlanmamış.")
            return
            
        try:
            client = genai.Client(api_key=API_KEY)
            
            # 3. API'ye sorgu gönder
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt
            )
            
            # 4. Başarılı yanıt gönder
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') # CORS ayarı: Her yerden çağrılabilir.
            self.end_headers()
            
            response_data = {
                "text": response.text,
                "status": "success"
            }
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_error_response(500, f"Gemini API hatası: {str(e)}")

    def send_error_response(self, code, message):
        """Hata mesajı göndermek için yardımcı fonksiyon."""
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_data = {
            "error": message,
            "status": "error"
        }
        self.wfile.write(json.dumps(error_data).encode('utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Gemini Proxy Hazır. POST isteği bekliyor.".encode('utf-8'))
