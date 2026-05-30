const sourceEditButtons = document.querySelectorAll('.source-edit');

// Attach a click event listener to each  Source Edit button
sourceEditButtons.forEach(button => {
    button.addEventListener('click', function() {
        // Regular function used intentionally — 'this' refers to the clicked button
        // Arrow functions do not bind 'this' and would return undefined here
        // Read the data-id from the clicked button
        const pk = this.dataset.id;
        // Fetches the form fragment from the server
        // Makes an asynchronous HTTP GET request to the URL
        fetch(`/sources/${pk}/edit/`)
            // Waits for the response and converts it to plain text
            .then(response => response.text())
            // Inject the returned HTML into the modal body
            .then(html => {
                document.querySelector('#editSourceModal .modal-body').innerHTML = html;
            });

    });
});
