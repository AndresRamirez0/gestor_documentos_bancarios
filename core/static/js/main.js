// Muestra en consola que el script carga
console.log('main.js ejecutándose');

const togglePassword   = document.getElementById('togglePassword');
const passwordField    = document.getElementById('password');

console.log('togglePassword, passwordField →', togglePassword, passwordField);

if (togglePassword && passwordField) {
  togglePassword.addEventListener('click', function () {
    // Alternar el tipo de input
    const isPassword = passwordField.type === 'password';
    passwordField.type = isPassword ? 'text' : 'password';

    // Cambiar icono
    this.classList.toggle('bi-eye');
    this.classList.toggle('bi-eye-slash');
  });
} else {
  console.warn('No se encontró el elemento togglePassword o passwordField');
}
