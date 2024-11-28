
document.getElementById('registerForm')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    if (email && password) {
     
        localStorage.setItem('userEmail', email);
        localStorage.setItem('userPassword', password);

       
        alert('Cuenta creada exitosamente');
        window.location.href = 'login.html';
    } else {
        alert('Por favor, complete todos los campos.');
    }
});

