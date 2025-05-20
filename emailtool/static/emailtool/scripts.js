document.addEventListener('DOMContentLoaded', function () {
    const toggles = document.querySelectorAll('.toggle-submenu');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            const submenu = this.nextElementSibling;
            submenu.classList.toggle('hidden');
        });
    });
});
