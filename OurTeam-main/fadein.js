document.addEventListener('scroll', function() {
    const fadeElements = document.querySelectorAll('.fade-in');

    fadeElements.forEach(function(element) {
        const rect = element.getBoundingClientRect();
        const inView = rect.top <= window.innerHeight && rect.bottom >= 0;

        if (inView) {
            element.classList.add('visible');
        }
    });
});
