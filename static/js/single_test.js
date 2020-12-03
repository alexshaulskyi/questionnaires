var questions_pool
var current_question = 0

function selectOption () {

    $('.option_checkbox_checked').removeClass('option_checkbox_checked').addClass('option_checkbox')
    $(this).removeClass('option_checkbox').addClass('option_checkbox_checked')

}

function appendQuestionProperties () {

    let question_number = current_question + 1
    let question_text = questions_pool[current_question]['text']
    let question_options = questions_pool[current_question]['options']

    $('.test_question_id').append('#  ' + question_number)
    $('.test_question_text').append(question_text)

    for (let i = 0; i < question_options.length; i++) {

        $('.question_options').append('<div id="single_option' + i + '" class="question_single_option">  </div>')
        $('#single_option' + i).append('<div class="question_options_checkbox"> <input type="checkbox" class="option_checkbox" value="' + question_options[i]['id'] + '"> </div>')
        $('#single_option' + i).append('<div class="question_options_text">' + question_options[i]['text'] + '</div>')
    }

}

function getInitialTestStatus () {

    let relation_id = $('#user_test_relation_id').attr('value')

    $.ajax({

        url: 'http://127.0.0.1:8000/api/v1/userpassedtest/' + relation_id +'/',
        type: 'get',
        dataType: 'json',
        success: function (data) {

            if (data.is_completed) {

                let test_id = $('#test_id').attr('value')

                $('.test_question').prepend('Вы уже прошли этот тест, посмотрите результаты в личном кабинете или запросите сброс, для того, чтобы пройти тест снова.')
                $('.start_test_button_container').empty()
                $('.start_test_button_container').append('<a class="finish_button" href="http://127.0.0.1:8000/test_results/' + test_id + '/"> Посмотреть результат </a>')

            } else {

                current_question = data.questions_answered_amount

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

function setCompleted () {

    var relation_id = $('#user_test_relation_id').attr('value')
    let token = $('#token').attr('value')
    
    $.ajax({

        headers: {
            'X-CSRFTOKEN': token
        },
        url: 'http://127.0.0.1:8000/api/v1/userpassedtest/' + relation_id + '/',
        type: 'patch',
        dataType: 'json',
        data: {'is_completed': true},
        success: function () {

            $.ajax({
                
                headers: {
                    'X-CSRFTOKEN': token
                },
                url: 'http://127.0.0.1:8000/api/v1/userpassedtest/set_score/',
                type: 'patch',
                dataType: 'json',
                data: {'relation_id': relation_id},
        
            })

        }

    })

}

function renderNextQuestion () {

    if ($('.option_checkbox_checked').length) {
        
        let option_id = $('.option_checkbox_checked').attr('value')
        let token = $('#token').attr('value')
        let relation_id = $('#user_test_relation_id').attr('value')
        let test_id = $('#test_id').attr('value')

        $.ajax({

            headers: {
                'X-CSRFTOKEN': token
            },
            url: 'http://127.0.0.1:8000/api/v1/userpassedtest/add_option/',
            type: 'patch',
            dataType: 'json',
            data: {'option_id': option_id, 'relation_id': relation_id},
            success: function () {

                current_question += 1

                if (!(current_question in questions_pool)) {

                    $('.test_question_id').empty()
                    $('.test_question_text').empty()
                    $('.question_options').empty()
                    $('.start_test_button_container').empty()
                    $('.start_test_button_container').append('<a class="finish_button" href="http://127.0.0.1:8000/test_results/' + test_id + '/"> Посмотреть результат </a>')
        
                    $('.test_question').prepend('Вы закончили тест, посмотрите результаты в личном кабинете')
        
                    setCompleted()

                } else {

                    $('.test_question_id').empty()
                    $('.test_question_text').empty()
                    $('.question_options').empty()

                    appendQuestionProperties()

                }

            }

        })

    } else {

        alert('Выберите ответ')

    }

}


$(document).ready(getInitialTestStatus)
$('.start_test_button').click(getQuestions)
$(document).on('click', '.option_checkbox', selectOption)
$(document).on('click', '.answer_button', renderNextQuestion)
$(document).on('click', '.finish_button', finishTest)