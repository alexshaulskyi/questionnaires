function removeRelation () {

    let relation_id = $(this).attr('rel_id')
    let token = $('#token').attr('value')

    $.ajax({

        headers: {
            'X-CSRFTOKEN': token
        },
        url: 'http://127.0.0.1:8000/api/v1/userpassedtest/' + relation_id + '/',
        type: 'delete',
        success: function () {

            $('#user_result_' + relation_id).remove()

        }

    })

}

$('.remove_relation_button').click(removeRelation)