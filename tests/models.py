from django.db import models

from users.models import User


class Test(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(default='quiz.png')
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tests'
    )

    def __str__(self):
        return self.name


class Question(models.Model):

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.CharField(max_length=800)

    def __str__(self):
        return str(self.pk)


class Option(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options'
    )
    text = models.CharField(max_length=800)
    is_correct = models.BooleanField()

    def __str__(self):
        return str(self.pk)


class UserPassedTest(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='passed_tests'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='users_passed'
    )
    selected_options = models.ManyToManyField(
        Option,
        related_name='selected_options',
        blank=True
    )
    score = models.CharField(max_length=4, blank=True)
    questions_answered_amount = models.IntegerField(blank=True, default=0)
    questions_answered = models.ManyToManyField(
        Question,
        related_name='answered_questions',
        blank=True
    )
    is_completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} passed {self.test.name}'
