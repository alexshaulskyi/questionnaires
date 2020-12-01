var questions_pool
var current_question = 0

function getInitialTestStatus () {

    let test_id = $('#test_id').attr('value')

    $.ajax({

        url: 'http://127.0.0.1:8000/api/get_initial_status/',
        type: 'get',
        dataType: 'json',
        data: {'test_id': test_id},
        success: function (data) {

            if (data.is_completed) {

                $('.test_question').prepend('Вы уже прошли этот тест, посмотрите результаты в личном кабинете или запросите сброс, для того, чтобы пройти тест снова.')

            } else {

                current_question = data.start_from_question

                if (current_question != 0) {

                    $.ajax({

                        url: 'http://127.0.0.1:8000/api/get_questions/',
                        type: 'get',
                        dataType: 'json',
                        data: {'test_id': test_id},
                
                        success: function (data) {
                
                            questions_pool = data

                            appendQuestionProperties()

                            $('.start_test_button_container').empty()
                            $('.start_test_button_container').append('<button class="answer_button"> Ответить </button>')
                
                        }

                    })

                }

            }

        }

    })

}

function selectOption () {

    $('.option_checkbox_checked').removeClass('option_checkbox_checked').addClass('option_checkbox')
    $(this).removeClass('option_checkbox').addClass('option_checkbox_checked')

}

function appendQuestionProperties () {

    let question_id = questions_pool[current_question]['id']
    let question_text = questions_pool[current_question]['text']
    let question_options = questions_pool[current_question]['options']

    $('.test_question_id').append('#  ' + question_id)
    $('.test_question_text').append(question_text)

    for (let i = 0; i < question_options.length; i++) {

        $('.question_options').append('<div id="single_option' + i + '" class="question_single_option">  </div>')
        $('#single_option' + i).append('<div class="question_options_checkbox"> <input type="checkbox" class="option_checkbox" value="' + question_options[i]['id'] + '"> </div>')
        $('#single_option' + i).append('<div class="question_options_text">' + question_options[i]['text'] + '</div>')
    }

}

function getQuestions () {

    let test_id = $('#test_id').attr('value')

    $.ajax({

        url: 'http://127.0.0.1:8000/api/get_questions/',
        type: 'get',
        dataType: 'json',
        data: {'test_id': test_id},

        success: function (data) {

            questions_pool = data

            appendQuestionProperties()

            $('.start_test_button_container').empty()
            $('.start_test_button_container').append('<button class="answer_button"> Ответить </button>')

        }
    })
}

function renderNextQuestion () {

    if ($('.option_checkbox_checked').length) {
        
        let option_id = $('.option_checkbox_checked').attr('value')
        let test_id = $('#test_id').attr('value')
        let token = $('#token').attr('value')

        $.ajax({

            url: 'http://127.0.0.1:8000/api/add_selected_option/',
            type: 'post',
            dataType: 'json',
            data: {'csrfmiddlewaretoken': token, 'option_id': option_id, 'test_id': test_id},
            success: function (data) {
                
                console.log(data)

            }

        })
        
        if (current_question + 1 === questions_pool.length) {

            $('.test_question_id').empty()
            $('.test_question_text').empty()
            $('.question_options').empty()
            $('.start_test_button_container').empty()
            $('.start_test_button_container').append('<button class="finish_button"> Вернуться на главную </button>')

            $('.test_question').prepend('Вы закончили тест, посмотрите результаты в личном кабинете')

            $.ajax({

                url: 'http://127.0.0.1:8000/api/set_completed/',
                type: 'post',
                dataType: 'json',
                data: {'csrfmiddlewaretoken': token, 'test_id': test_id}

            })

        } else {

            current_question += 1

            $('.test_question_id').empty()
            $('.test_question_text').empty()
            $('.question_options').empty()

            appendQuestionProperties()

        }

        

    } else {

        alert('Выберите ответ')

    }

}


$(document).ready(getInitialTestStatus)
$('.start_test_button').click(getQuestions)
$(document).on('click', '.option_checkbox', selectOption)
$(document).on('click', '.answer_button', renderNextQuestion)