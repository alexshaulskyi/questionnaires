from django import template

from users.models import NotifySuperuser

register = template.Library()

@register.filter(name="get_notification_status")
def get_notification_status():

    obj = NotifySuperuser.objects.get(id=1)

    return obj.flag