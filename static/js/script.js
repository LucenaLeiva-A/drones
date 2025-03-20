// Carrusel de fondo
window.addEventListener("load", function() {
  const images = document.querySelectorAll(".carousel img");
  let current = 0;
  setInterval(() => {
    images[current].classList.remove("active");
    current = (current + 1) % images.length;
    images[current].classList.add("active");
  }, 3000);
});

// Mostrar el nombre del usuario en la parte superior derecha si ha iniciado sesión
window.addEventListener("DOMContentLoaded", function() {
  const userInfo = document.getElementById("userInfo");
  const usuario = sessionStorage.getItem("usuario");
  if (usuario) {
    const userObj = JSON.parse(usuario);
    userInfo.innerText = "Bienvenido, " + userObj.nombre;
  }
});

// Manejo del menú desplegable de usuario
document.addEventListener("DOMContentLoaded", function() {
  const userMenuContainer = document.getElementById("userMenuContainer");
  const userInfo = document.getElementById("userInfo");

  if (userInfo) {
    userInfo.addEventListener("click", function(event) {
      event.stopPropagation(); // Evita que el clic se propague al documento
      userMenuContainer.classList.toggle("active");
    });
  }

  // Cerrar el menú si se hace clic fuera de él
  document.addEventListener("click", function(event) {
    if (!userMenuContainer.contains(event.target)) {
      userMenuContainer.classList.remove("active");
    }
  });
});