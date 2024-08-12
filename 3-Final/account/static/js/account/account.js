document.addEventListener('DOMContentLoaded', function() {
    // Function to handle login form submission
    function handleLogin() {
        const form = document.getElementById('login-form');
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(form);
            
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'logged_in') {
                    document.getElementById('login-form-container').style.display = 'none';
                    document.getElementById('logged-in-section').style.display = 'block';
                    document.getElementById('user-info').innerText = `Logged in as ${data.username}`;
                } else if (data.status === 'error') {
                    const errors = JSON.parse(data.errors);
                    const errorMessages = Object.values(errors).map(error => `<p>${error}</p>`).join('');
                    document.getElementById('form-errors').innerHTML = errorMessages;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Function to handle logout button click
    function handleLogout() {
        const logoutButton = document.getElementById('logout-button');
        logoutButton.addEventListener('click', function() {
            fetch('/account/logout/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'logged_out') {
                    document.getElementById('login-form-container').style.display = 'block';
                    document.getElementById('logged-in-section').style.display = 'none';
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Initial function calls
    handleLogin();
    handleLogout();
});
