
document.addEventListener('DOMContentLoaded', function () {
    const toggler = document.querySelector('.navbar-toggler');
    const icon = document.getElementById('navToggleIcon');

    toggler.addEventListener('click', function () {
        // Wait for the collapse animation to complete (~100ms)
        setTimeout(() => {
            const isExpanded = toggler.getAttribute('aria-expanded') === 'true';

            // Change icon based on state
            if (isExpanded) {
                icon.classList.remove('fa-book');
                icon.classList.add('fa-book-open');
            } else {
                icon.classList.remove('fa-book-open');
                icon.classList.add('fa-book');
            }
        }, 100);
    });
});
