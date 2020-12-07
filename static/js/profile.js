function startNotifications () {

    $.ajax({

        url: 'http://127.0.0.1:8000/auth/notify_superuser/',
        type: 'get',
        success: function (data) {

            console.log(data)

        }

    })

}

$('.start_notifications_button').click(startNotifications)