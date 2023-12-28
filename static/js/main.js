var header = document.getElementById("main-header");
var lastScrollTop = 0;

// Obtén la posición inicial del header
var sticky = header.offsetTop;

function stickyHeader() {
    var currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScrollTop == 0) {
        // En la parte superior de la página
        header.style.position = "relative";  // Puedes establecer la posición que desees aquí
        header.style.display = "flex";
    } else if (currentScrollTop < lastScrollTop) {
        // Scroll hacia arriba
        header.style.position = "fixed";
        header.style.display = "flex";
    } else if (currentScrollTop > lastScrollTop) {
        // Scroll hacia abajo
        header.style.position = "relative";  // Puedes establecer la posición que desees aquí
        header.style.display = "flex";
    }
    lastScrollTop = currentScrollTop;
}

// Adjunta la función al evento de scroll
window.onscroll = function() {
    stickyHeader();
};