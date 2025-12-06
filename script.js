document.addEventListener('DOMContentLoaded', () => {
// Mobile menu toggle
const menuToggle = document.getElementById('mobile-menu');
const navbar = document.getElementById('navbar');

```
menuToggle.addEventListener('click', () => {
    navbar.classList.toggle('active');
});

// Toggle place detail
const titles = document.querySelectorAll('.place-title');

titles.forEach(title => {
    title.addEventListener('click', () => {
        const targetId = title.dataset.target;
        const detail = document.getElementById(targetId);
        detail.classList.toggle('open');
    });
});
```

});
document.addEventListener('DOMContentLoaded', () => {

    const message = document.getElementById('school-message');
    const closeBtn = document.getElementById('close-message');
    const arrow = document.getElementById('reopen-arrow');

    // Mesajı kapatma
    closeBtn.addEventListener('click', () => {
        message.style.display = 'none';
        arrow.style.display = 'block';
    });

    // Mesajı tekrar açma
    arrow.addEventListener('click', () => {
        message.style.display = 'block';
        arrow.style.display = 'none';
    });

});
document.addEventListener('DOMContentLoaded', () => {

    const message = document.getElementById('school-message');
    const closeBtn = document.getElementById('close-message');
    const arrow = document.getElementById('reopen-arrow');

    closeBtn.addEventListener('click', () => {
        message.style.display = 'none';
        arrow.style.display = 'block';
    });

    arrow.addEventListener('click', () => {
        message.style.display = 'block';
        arrow.style.display = 'none';
    });

});
// MOBIL MENU
const mobileMenu = document.getElementById("mobile-menu");
const navbar = document.getElementById("navbar");

if (mobileMenu) {
    mobileMenu.addEventListener("click", () => {
        navbar.classList.toggle("active");
    });
}

