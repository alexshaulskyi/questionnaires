from django.contrib import admin

from users.models import User, NotifySuperuser

class UserAdmin(admin.ModelAdmin):

    model = User

class NotifyAdmin(admin.ModelAdmin):

    model = NotifySuperuser


admin.site.register(User, UserAdmin)
admin.site.register(NotifySuperuser, NotifyAdmin)