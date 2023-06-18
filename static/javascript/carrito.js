
let lista = [];
let valortotal = 0;

// Funciones para almacenar y obtener los datos del carrito desde el almacenamiento local
function guardarAlmacenamientoLocal(llave, valor_a_guardar) {
  localStorage.setItem(llave, JSON.stringify(valor_a_guardar));
}

function obtenerAlmacenamientoLocal(llave) {
  const datos = JSON.parse(localStorage.getItem(llave));
  return datos;
}

// Obtener la lista de productos del almacenamiento local (si existe)
lista = obtenerAlmacenamientoLocal('productos') || [];

// Variables que traemos de nuestro HTML
const carritoEnlace = document.querySelector('.carrito-enlace');
const badge = document.querySelector('.badge');

// Actualizar el número en el badge del carrito
function actualizarBadge() {
  if (lista.length > 0) {
    badge.textContent = lista.length;
    badge.style.display = 'inline-block';
  } else {
    badge.style.display = 'none';
  }
}

// Función para agregar un producto al carrito
function agregarAlCarrito(producto) {
  lista.push(producto);
  guardarAlmacenamientoLocal('productos', lista);
  actualizarBadge();
}

// Evento clic en el enlace del carrito
carritoEnlace.addEventListener('click', function(event) {
  event.preventDefault();
  // Aquí puedes realizar alguna acción adicional al hacer clic en el enlace del carrito
  // Por ejemplo, mostrar el contenido del carrito en un modal o redirigir a la página del carrito
});

// Ejemplo de uso de la función agregarAlCarrito:
const productos = [
    {% for p in productos %}
    {
      titulo: "{{ p.titulo }}",
      precio: {{ p.precio }},
      descripcion: "{{ p.descripcion }}",
      id_categoria: "{{ p.id_categoria }}"
    },
    {% empty %}
    // No hay productos en el carrito
    {% endfor %}
  ];

agregarAlCarrito(producto);
