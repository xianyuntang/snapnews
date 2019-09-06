let submit_form_and_restart_service = function () {

    $.ajax({
        url: "/setting/POST/restart_service/",
        method: 'POST',
        dataType: 'json',
    });
};