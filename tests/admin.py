from django.contrib import admin

from tests.models import Test, Question, Option, UserPassedTest

class TestAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'pub_date', 'author')
    search_fields = ('author', 'name')
    list_filter = ('author', 'pub_date')
    empty_value_display = '-пусто-'


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('pk', 'test', 'text')


class OptionAdmin(admin.ModelAdmin):

    list_display = ('pk', 'question', 'text', 'is_correct')


class UserPassedTestAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'test')
    search_fields = ('user', 'test')
    list_filter = ('user', 'test', 'is_completed')
    empty_value_display = '-пусто-'


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(UserPassedTest, UserPassedTestAdmin)
