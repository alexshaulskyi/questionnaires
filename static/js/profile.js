function startNotifications () {

    $.ajax({

        url: 'http://127.0.0.1:8000/auth/notify_superuser/',
        type: 'get',
        success: function (data) {

            if (data.success === 'started') {

                $('.start_notifications_button').empty()
                $('.start_notifications_button').append('Прекратить оповещения')

            } else if (data.success === 'stopped') {

                $('.start_notifications_button').empty()
                $('.start_notifications_button').append('Начать оповещение')

            }

        }

    })

}

$('.start_notifications_button').click(startNotifications)