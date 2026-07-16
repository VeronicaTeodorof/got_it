// ===== Layout =====
// Set navbar height CSS variable for sidebar offset
const navbar = document.querySelector('.navbar');
document.documentElement.style.setProperty('--navbar-height', navbar.offsetHeight + 'px');

// ===== Event Listeners =====
// Add event listeners to 'cancel-form' buttons to reset forms without page reload
const cancelButton = document.querySelectorAll('[data-action="cancel-form"]')
cancelButton.forEach(button => {
    button.addEventListener('click', function() {
        // closest() is a method available on any element, that walks up the DOM tree until
        // it finds an ancestor matching the selector, in this case - 'form'
        const form = this.closest('form');
        // form.reset() isn't used here because it resets fields to
        // their current value attribute, not to blank — after an
        // invalid submission, Django re-renders the field with the
        // submitted value in, so reset() would just restore
        // that same value instead of clearing it.
        // 'hidden' is skipped to avoid wiping the CSRF token.
        form.querySelectorAll('input, select, textarea').forEach(el => {
            if (el.type === 'submit' || el.type === 'button' || el.type === 'hidden') return;
            el.value = '';
        });
        // remove server-rendered error lists (Django's .errorlist,
        // not crispy-forms' old .invalid-feedback)
        form.querySelectorAll('.errorlist').forEach(el => el.remove());
    });
})

// Toggle sidebar width
// Guarded because the sidebar (and its toggle) don't exist in the DOM
// when there are no sources yet — empty state hides the whole sidebar
const masterToggle = document.querySelector('.sidebar-master-toggle');
const sidebar = document.getElementById('appSidebar');

if (masterToggle && sidebar) {
    masterToggle.addEventListener('click', () => {
      sidebar.classList.toggle('expanded-sidebar');
  });
};

// Close sidebar
// Same empty-state guard as above — closeBtn won't exist if the sidebar
// itself isn't rendered, so skip attaching the listener entirely.
const closeBtn = document.querySelector('.sidebar-close');

if (closeBtn) {
  closeBtn.addEventListener('click', () => {
    sidebar.classList.remove('expanded-sidebar');
    document.querySelector('.sidebar-master-toggle').classList.remove('is-expanded');

    document.querySelectorAll('.sidebar .collapse.show').forEach(el => {
      // `getOrCreateInstance` safely fetches whatever instance
      // Bootstrap already made for that element
      // and only creates a fresh one as a fallback if somehow none exists yet
      bootstrap.Collapse.getOrCreateInstance(el).hide();
    });
  });
}

// ===== Forms =====
// Show forms expanded when they contain errors
const expandForms = document.querySelectorAll('.expand-on-error')
expandForms.forEach(form => {
    if (form.querySelector('.errorlist')) {
        form.classList.add('show');
        form.classList.remove('collapse');
    }
})

// ===== Tooltips =====
// Initializes Bootstrap tooltips
const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]')
tooltips.forEach(el => new bootstrap.Tooltip(el))



