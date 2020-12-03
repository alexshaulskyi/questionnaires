### Questionnaires.

Place where people may pass different tests.

#### Description.

Platform which lets you to create and pass tests. 

Main features:

* Unlimited amount of questions per test.
* Unlimited amount of options per question.
* Only one correct option per question tho.
* Should connection drop, test will start from the first question which was not answered.
* Users can see detailed test results after passing one.
* Superusers can reset test results for any user in order to let them pass a test again.
* Users can modify their profiles.
* Handy filters in django admin panel.

Main tech features:

* Questions are loaded asynchronously with AJAX (Djquery + DRF)
* Results reset is asynchronous as well.
* Application is stored in 2 Docker containers. 1 command is required to start.
* A background thread is set to notify selected user with statistics daily.

#### Start

* Run docker-compose up --build.
* Apply migrations.
* Create superuser.

That's basically it.

#### Usage.

Tests can be created in default django admin panel. Test, Question and Option models are related, thus first create a test, then questions for it and then options for each question.
Mark correct option as correct. Once done, test will appear on index page. Users must be registered in order to pass test. Despite index page looks the same to both users and superusers
once first proceeds to selected test, he will see an option to load it's questions and pass the test. Superusers, on other hand, will be able to see the results of all users who passed this test
as well as an option to reset test results for a selected user. Both users and superusers may edit their profile, but unlike superusers, users will also be able to browse all tests
they have passed and display the detailed results of them.

