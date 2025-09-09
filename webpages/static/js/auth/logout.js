$("#logout").click(function (e) {
    e.preventDefault();
    const csrftoken = getCookie("csrftoken");
    $.ajax({
        url: BASE_URL + "api/auth/logout/session/",
        type: "POST",
        headers: {"X-CSRFToken": csrftoken},
        dataType: "json",
        success: function (response) {
            window.location.href = "/login";
        },
        error: function (xhr) {
            alert("Login failed: " + xhr.responseText);
        }
    });
});