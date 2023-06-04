var mensajeError =[];
var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var apellido2 = document.getElementById('apellido2');
var telefono = document.getElementById('telefono');
var email = document.getElementById('email');
var password = document.getElementById('password');
var confirmPassword = document.getElementById('password2');

var form = document.getElementById('formulario');
form.addEventListener('submit', function(evt){
    evt.preventDefault();  
    
    document.getElementById('nombreError').innerHTML = "";
    document.getElementById('apellidoError').innerHTML = "";
    document.getElementById('apellido2Error').innerHTML = "";
    document.getElementById('telefonoError').innerHTML = "";
    document.getElementById('emailError').innerHTML = "";
    document.getElementById('passwordError').innerHTML = "";
    document.getElementById('passwordError2').innerHTML = "";
  
    var emailValidado = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    if (!emailValidado.test(email.value)) {
        mensajeError.push("Por favor ingresa un email válido.");
    }

    if(nombre.value === null || nombre.value === ""){
        document.getElementById('nombreError').innerHTML =("Debes poner un Nombre");
    }
    if(nombre.value.length < 3 && nombre.value.length < 20){
        document.getElementById('nombreError').innerHTML =("El nombre debe tener al menos 3 y no mas de 20 caracteres ");
    }

    if(apellido.value === null || apellido.value === ""){
        document.getElementById('apellidoError').innerHTML = ("Debes poner un Apellido");
    }
    if(apellido.value.length < 3 && apellido.value.length < 20){
        document.getElementById('apellidoError').innerHTML = ("El Apellido paterna debe tener al menos 3 y no mas de 20 caracteres");
    }

    if(apellido2.value ===null || apellido2.value === ""){
        document.getElementById('apellido2Error').innerHTML = ("Debes poner un Apellido");
    }
    if(apellido2.value.length < 3 && apellido2.value.length < 20){
        document.getElementById('apellido2Error').innerHTML = ("El Apellido materna debe tener al menos 3 y no mas de 20 caracteres");
    }

    if(telefono.value.length < 9 && telefono.value.length < 12){
        document.getElementById('telefonoError').innerHTML = ("N°telefono no Valido");
    }

    if(email.value === null || email.value === '' ){
        document.getElementById('emailError').innerHTML = ("Debe ingresa un Correo");
    }

    if(password.value === null ||password.value === '' ){
        document.getElementById('emailError').innerHTML = ("Debe ingresa tu passord");
    }
    if(password.value.length <= 6){
        document.getElementById('passwordError').innerHTML = ("La Contraseña debe tener mas de 6 caracteres");
    }

    if (password.value !== confirmPassword.value){
        document.getElementById('passwordError2').innerHTML = ("Las contraseña son diferents");
    }
    
    setTimeout(function() {
        document.getElementById('nombreError').innerHTML = "";
        document.getElementById('apellidoError').innerHTML = "";
        document.getElementById('apellido2Error').innerHTML = "";
        document.getElementById('telefonoError').innerHTML = "";
        document.getElementById('emailError').innerHTML = "";
        document.getElementById('passwordError').innerHTML = "";
        document.getElementById('passwordError2').innerHTML = "";
      }, 5000);

      function verificarCampos() {
        var apellidoValue = apellido.value.trim();
        var apellido2Value = apellido2.value.trim();
        var nombreValue = nombre.value.trim();
        var telefonoValue = telefono.value.trim();
        var emailValue = email.value.trim();
        var passwordValue = password.value.trim();
        var confirmPasswordValue = confirmPassword.value.trim();
      
        if (
          apellidoValue !== '' &&
          apellido2Value !== '' &&
          nombreValue !== '' &&
          telefonoValue !== '' &&
          emailValue !== '' &&
          passwordValue !== '' &&
          confirmPasswordValue !== ''
        ) {
          form.removeAttribute('id');
          document.getElementById('nombreError').innerHTML = '';
          document.getElementById('apellidoError').innerHTML = '';
          document.getElementById('apellido2Error').innerHTML = '';
          document.getElementById('telefonoError').innerHTML = '';
          document.getElementById('emailError').innerHTML = '';
          document.getElementById('passwordError').innerHTML = '';
          document.getElementById('passwordError2').innerHTML = '';
        }
      }
      
      apellido.addEventListener('input', verificarCampos);
      apellido2.addEventListener('input', verificarCampos);
      nombre.addEventListener('input', verificarCampos);
      telefono.addEventListener('input', verificarCampos);
      email.addEventListener('input', verificarCampos);
      password.addEventListener('input', verificarCampos);
      confirmPassword.addEventListener('input', verificarCampos);  
})

  