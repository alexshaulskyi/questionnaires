function createUserTestRelation (event) {

    event.preventDefault()

    let test_id = $(this).attr('identifier')
    let token = $('#token').attr('value')

    $.ajax({

        url: 'http://127.0.0.1:8000/api/create_relation/',
        type: 'post',
        dataType: 'json',
        data: {'test_id': test_id, 'csrfmiddlewaretoken': token},
        success: function () {

            $(location).attr('href', 'http://127.0.0.1:8000/' + test_id + '/');

        },

        error: function(data) {

            console.log(data)

            $(location).attr('href', 'http://127.0.0.1:8000/' + test_id + '/');

        }

    })

}

$('.index_link').click(createUserTestRelation)