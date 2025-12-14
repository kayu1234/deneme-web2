import os
import json
from google import genai
from http.server import BaseHTTPRequestHandler

# API Anahtarı Kasanın içinden çekilir (SENİN ASLA GÖRMEDİĞİN GİZLİ ŞİFRE)
API_KEY = os.environ.get("GEMINI_API_KEY")

class handler(BaseHTTPRequestHandler):
    """
    Bu, Vercel'in çalıştırdığı Kapıcının ta kendisidir.
    """

    def do_POST(self):
        # Müşteriden (Web sitesinden) gelen soruyu oku
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            user_prompt = data.get('prompt', 'Merhaba, nasılsın?')
        except:
            self.send_error(400)
            return

        # Yapay Zeka Şifresi olmadan iş yapmayız
        if not API_KEY:
            self.send_error(500)
            return
            
        try:
            # Yapay Zeka Mutfağı'na soruyu ilet
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt
            )
            
            # Cevabı siteye geri gönder
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') # Herkes sorabilir
            self.end_headers()
            
            response_data = {"text": response.text, "status": "success"}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception:
            self.send_error(500)

    # Vercel'in doğru çalıştığını kontrol etme kodu (Önemli değil)
    def do_GET(self):
        self.send_response(200); self.send_header('Content-type', 'text/plain'); self.end_headers()
        self.wfile.write("Kapıcı Hazır. Sorunuzu bekliyor.".encode('utf-8'))