
function handleScroll() {
    const scrollTrigger = 1;
    const header = document.querySelector('header');
    // Comprobar si la posición de scroll vertical (pageYOffset) es mayor que el punto de activación
    if (window.pageYOffset > scrollTrigger) {
        // Si el scroll está activado, añadir la clase 'scrolled'
        header.classList.add('scrolled');
    } else {
        // Si volvemos a la parte superior, quitar la clase 'scrolled'
        header.classList.remove('scrolled');
    }
}

// 4. Escuchar el evento 'scroll' y ejecutar la función
window.addEventListener('scroll', handleScroll);
