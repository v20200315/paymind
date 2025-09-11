$(function () {
    $("#login_form").submit(function (e) {
        e.preventDefault();
        const csrftoken = getCookie("csrftoken");
        const formData = {
            phone: $('input[name="phone"]').val().trim(),
            password: $('input[name="password"]').val().trim(),
        };
        const remember = $('input[name="remember"]').is(':checked')
        $.ajax({
            url: BASE_URL + "api/auth/login/session/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            headers: {"X-CSRFToken": csrftoken},
            dataType: "json",
            success: function (response) {
                console.log("login success:", response);
                localStorage.setItem("token", response.token);
                localStorage.setItem("refresh", response.refresh);
                const urlParams = new URLSearchParams(window.location.search);
                const nextUrl = urlParams.get("next") || "/dashboard";
                window.location.href = nextUrl;
            },
            error: function (xhr) {
                alert("Login failed: " + xhr.responseText);
            }
        });
        if (remember) {
            console.log("remember me");
        }
    });
});