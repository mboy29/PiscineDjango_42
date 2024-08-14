$(document).ready(function() {
    $('#login-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: loginUrl,
            data: $(this).serialize(),
            success: function(response) {
                if (response.status === 'success') {
                    location.reload();
                } else {
                    $('#form-errors').html('');
                    $.each(response.errors, function(field, errors) {
                        $('#form-errors').append('<p>' + errors[0] + '</p>');
                    });
                }
            }
        });
    });

    $('#logout-button').on('click', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: logoutUrl,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.status === 'success') {
                    location.reload();
                }
            }
        });
    });
});

$(document).ready(function() {
    $('#navbar-logout').on('click', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: logoutUrl,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.status === 'success') {
                    location.reload();
                }
            }
        });
    });
});
