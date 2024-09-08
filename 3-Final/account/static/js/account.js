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
                    $('#chat-section').show();
                } else {
                    $('#login-section').show();
                    $('#logout-section').hide();
                    $('#chat-section').hide();
                }
            },
            error: function() {
                $('#username').value = '';
                $('#password').value = '';
                $('#login-section').show();
                $('#logout-section').hide();
                $('#chat-section').hide();
            }
        });
    }

    $('#login-form').on('submit', function(event) {
        event.preventDefault();

        $('#form-errors').empty();

        $.ajax({
            type: 'POST',
            url: loginUrl,
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    updatePage();
                    $('#password').val('');
                    $('#username').val('');
                } else {
                    $('#form-errors').html('Invalid username or password.');
                }
            },
            error: function() {
                $('#form-errors').html('An error occurred while trying to log in.');
            },
        });
    });

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
                $('#form-errors').html('An error occurred while trying to log out.');
            }
        });
    });

    updatePage();
});
