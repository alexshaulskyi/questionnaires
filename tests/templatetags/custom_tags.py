from django import template

from tests.models import Test, UserPassedTest
from users.models import User


register = template.Library()

@register.filter(name='relation_exists')
def relation_exists(test, request):
    obj, created = UserPassedTest.objects.get_or_create(
        user=request.user,
        test=test
    )

    return obj.id
