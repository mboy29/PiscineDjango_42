$(document).ready(function() {
    function updatePage() {
        $.ajax({
            type: 'GET',
            url: statusUrl,
            success: function(response) {
                if (response.success && response.user_is_authenticated) {
                    $('#login-section').hide();
                    $('#logout-section').show();
                    $('#user-info').text('Logged as ' + response.username);
                } else {
                    $('#login-section').show();
                    $('#logout-section').hide();
                }
            },
            error: function() {
                // Handle errors if needed
                $('#login-section').show();
                $('#logout-section').hide();
            }
        });
    }

    $('#login-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: loginUrl,
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    updatePage();
                } else {
                    $('#error-message').html('Invalid username or password.');
                }
            },
            error: function() {
                $('#error-message').html('An error occurred while trying to log in.');
            }
        });
    });

    // Handle logout button click
    $('#logout-btn').on('click', function() {
        $.ajax({
            type: 'POST',
            url: logoutUrl,
            success: function(response) {
                if (response.success) {
                    updatePage();
                }
            },
            error: function() {
            }
        });
    });

    // Initial page load
    updatePage();
});