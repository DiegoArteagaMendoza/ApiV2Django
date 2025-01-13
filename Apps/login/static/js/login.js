document.addEventListener('DOMContentLoaded', function() {
    // Ejemplo básico para validar el formulario
    const form = document.querySelector('.login-form');

    form.addEventListener('submit', function(e) {
        const userRut = document.querySelector('input[name="userRut"]').value;
        const password = document.querySelector('input[name="password"]').value;

        if (!userRut || !password) {
            e.preventDefault();
            alert('Por favor, complete todos los campos.');
        }
    });
});
