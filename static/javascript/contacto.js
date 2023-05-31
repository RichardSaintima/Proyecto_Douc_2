const form = document.getElementById('form');
 const nombre = document.getElementById('nombre');
 const telefono = document.getElementById('telefono');
 const email = document.getElementById('email');
 const mensaje = document.getElementById('mensaje');

 form.addEventListener('submit', e =>{
    e.preventDefault();

    validateInputs();
 });

 const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
 }

 const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
 };

 const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
 }


 const validateInputs = () => {
    const nameValue = nombre.value.trim();
    const telefonoValue = telefono.value.trim();
    const emailValue = email.value.trim();
    const mensajeValue = mensaje.value.trim();

    if (nameValue === ''){
        setError(nombre, 'Ingrese su nombre');
    } else {
        setSuccess(nombre);
    }

    if(telefonoValue === '') {
        setError(telefono, 'Ingrese su número');
    } else if (telefonoValue.length < 9 ) {
        setError(telefono, 'Su número debe contener al menos 9 dígitos')
    } else {
        setSuccess(telefono);
    }

    if(emailValue === '') {
        setError(email, 'Ingrese un email');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Ingrese un email válido');
    } else {
        setSuccess(email);
    }

    if (mensajeValue === ''){
        setError(mensaje, 'Ingrese su mensaje');
    } else if(mensajeValue.length < 25){
        setError(mensaje, 'Su mensaje debe contener al menos 25 caracteres')
    } else{    
        setSuccess(mensaje);
    }
 };
