$("#registerForm").submit(function (e) {
    e.preventDefault();
    const csrftoken = getCookie("csrftoken");
    const formData = {
        email: $('input[name="email"]').val().trim(),
        phone: $('input[name="phone"]').val().trim(),
        password: $('input[name="password"]').val().trim(),
    };
    const terms = $('input[name="terms"]').is(':checked')
    if (terms) {
        $.ajax({
            url: BASE_URL + "api/auth/register/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            headers: {"X-CSRFToken": csrftoken},
            dataType: "json",
            success: function (response) {
                console.log("register success:", response);

                localStorage.setItem("token", response.token);

                window.location.href = "/login";
            },
            error: function (xhr) {
                alert("Login failed: " + xhr.responseText);
            }
        });
    } else {
        alert("Please agree to the terms and register");
    }
});