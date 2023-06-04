// Agregar evento de clic a los botones "Añadir al Carrito"
var botonesAgregarCarrito = document.getElementsByClassName('btn-agregar-carrito');
for (var i = 0; i < botonesAgregarCarrito.length; i++) {
  botonesAgregarCarrito[i].addEventListener('click', function() {
    var productoId = this.getAttribute('data-producto-id');
  
    // Realizar una petición al servidor para agregar el producto al carrito
    agregarProductoAlCarrito(productoId);
  });
}

// Función para agregar el producto al carrito
function agregarProductoAlCarrito(productoId) {
  // Realizar una petición al servidor para agregar el producto al carrito
  // Puedes usar AJAX, fetch o cualquier otro método de tu elección
  // Aquí tienes un ejemplo utilizando fetch:

  fetch('/producto/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ productoId: productoId })
  })
  .then(function(response) {
    if (response.ok) {
      // El producto se agregó al carrito correctamente
      actualizarCantidadCarrito();
    } else {
      // Hubo un error al agregar el producto al carrito
      console.error('Error al agregar producto al carrito');
    }
  })
  .catch(function(error) {
    console.error('Error al realizar la solicitud', error);
  });
}

// Función para obtener la cantidad actual en el carrito
function obtenerCantidadCarrito() {
  // Realizar una petición al servidor para obtener la cantidad del carrito
  // Puedes usar AJAX, fetch o cualquier otro método de tu elección
  // Aquí tienes un ejemplo utilizando fetch:

  return fetch('/obtener-cantidad-carrito')
    .then(function(response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Error al obtener la cantidad del carrito');
      }
    })
    .then(function(data) {
      return data.cantidad;
    })
    .catch(function(error) {
      console.error('Error al obtener la cantidad del carrito', error);
      return 0; // Retorna 0 en caso de error
    });
}

// Función para actualizar la cantidad en el carrito en la interfaz
function actualizarCantidadCarrito() {
  var cantidadCarritoElemento = document.getElementById('cantidad-carrito');
  if (cantidadCarritoElemento) {
    obtenerCantidadCarrito()
      .then(function(cantidad) {
        cantidadCarritoElemento.textContent = cantidad;
      });
  }
}

// Actualizar la cantidad en el carrito al cargar la página
actualizarCantidadCarrito();