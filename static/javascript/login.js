var password = document.getElementById('password');
var email = document.getElementById('email');

var form = document.getElementById('formulario');
form.addEventListener('submit', function(evt) {
  evt.preventDefault();

  document.getElementById('emailError').innerHTML = "";
  document.getElementById('passwordError').innerHTML = "";

  var emailValidado = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  if (!emailValidado.test(email.value)) {
    document.getElementById('emailError').innerHTML = "Por favor ingresa un email válido.";
  }

  if (email.value === null || email.value === '') {
    document.getElementById('emailError').innerHTML = "Debe ingresar un Correo";
  }

  if (password.value === null || password.value === '') {
    document.getElementById('passwordError').innerHTML = "Debe ingresar tu password";
  }
  if (password.value.length <= 6) {
    document.getElementById('passwordError').innerHTML = "La Contraseña debe tener más de 6 caracteres";
  }
  
  setTimeout(function() {
    document.getElementById("emailError").innerHTML = "";
    document.getElementById("passwordError").innerHTML = "";
  }, 5000);
});

