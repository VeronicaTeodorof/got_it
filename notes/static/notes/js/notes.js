// ===== Layout =====
// Set navbar height CSS variable for sidebar offset
const navbar = document.querySelector('.navbar');
document.documentElement.style.setProperty('--navbar-height', navbar.offsetHeight + 'px');

// ===== Buttons =====
// Add event listeners to 'cancel-form' buttons to reset forms without page reload
const cancelButton = document.querySelectorAll('[data-action="cancel-form"]')
cancelButton.forEach(button => {
    button.addEventListener('click', function() {
        // closest() is a method available on any element, that walks up the DOM tree until
        // it finds an ancestor matching the selector, in this case - 'form'
        this.closest('form').reset();
    });
})

// ===== Forms =====
// Show forms expanded when they contain errors
const expandForms = document.querySelectorAll('.expand-on-error')
expandForms.forEach(form => {
    if (form.querySelector('.invalid-feedback')) {
        form.classList.add('show');
        form.classList.remove('collapse');
    }
})

// ===== Tooltips =====
// Initializes Bootstrap tooltips
const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]')
tooltips.forEach(el => new bootstrap.Tooltip(el))



