document.addEventListener('DOMContentLoaded', function() {
    // Get the form and toast elements
    const contactForm = document.getElementById('contactForm');
    const successToast = document.getElementById('successToast');
    
    // Initialize the toast
    const toastInstance = new bootstrap.Toast(successToast, {
        animation: true,
        autohide: true,
        delay: 3000
    });

    // Form submission handler
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        // Here you would typically send the data to your server
        // For now, we'll just simulate a successful submission
        console.log('Form Data:', formData);
        
        // Show success toast
        toastInstance.show();
        
        // Clear the form
        contactForm.reset();
    });
}); 