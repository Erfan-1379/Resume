$(document).ready(function () {
    $("#send_message").click(function (e) {
        e.preventDefault();

        var hasError = false;
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
        var message = $("#message").val();

        $("#name,#email,#phone,#message").click(function () {
            $(this).removeClass("error_input");
        });

        if (name.length == 0) {
            hasError = true;
            $("#name").addClass("error_input");
        } else {
            $("#name").removeClass("error_input");
        }

        if (email.length == 0 || email.indexOf("@") == -1) {
            hasError = true;
            $("#email").addClass("error_input");
        } else {
            $("#email").removeClass("error_input");
        }

        if (phone.length == 0) {
            hasError = true;
            $("#phone").addClass("error_input");
        } else {
            $("#phone").removeClass("error_input");
        }

        if (message.length == 0) {
            hasError = true;
            $("#message").addClass("error_input");
        } else {
            $("#message").removeClass("error_input");
        }

        if (!hasError) {
            $("#send_message").attr({
                disabled: "true",
                value: "Sending..."
            });

            var csrftoken = $("input[name='csrfmiddlewaretoken']").val();

            $.ajax({
                type: 'POST',
                url: $("#contact_form").attr('action'),
                data: $("#contact_form").serialize(),
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function (response) {
                    if (response.success) {
                        $("#submit").remove();
                        $("#mail_success").fadeIn(500);
                    } else {
                        $("#mail_fail").fadeIn(500);
                        $("#send_message").removeAttr("disabled").attr("value", "Submit Form");
                    }
                },
                error: function () {
                    $("#mail_fail").fadeIn(500);
                    $("#send_message").removeAttr("disabled").attr("value", "Submit Form");
                }
            });
        }
    });
});
