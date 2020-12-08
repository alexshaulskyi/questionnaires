import threading
from datetime import datetime, date
import time

from django.core.mail import send_mail
from django.views.generic import View
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Avg

from users.models import User, NotifySuperuser
from tests.models import UserPassedTest


class Notify(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        self.event = threading.Event()


    def notifier(self):

        now = datetime.now().strftime("%H:%M:%S")

        window_starts = '01:17:00'
        window_ends = '01:17:30'

        if window_starts < now < window_ends:

            tests_passed = UserPassedTest.objects.filter(date=date.today(), is_completed=True).count()
            av_score = UserPassedTest.objects.aggregate(Avg('score'))

            send_mail(
                'Stats for today', 
                f'Today {tests_passed} was passed with average score of {av_score}',
                'noreply@tests.com',
                ('testemail@test.com',),
                fail_silently=False
            )

            time.sleep(30)

    def run(self):

        while not self.event.is_set():
            
            self.notifier()

    def stop(self):

        self.event.set()


class NotifyView(View):

    def get(self, request):

        if not request.user.is_superuser:
            return redirect('index')
        
        obj, created = NotifySuperuser.objects.get_or_create(id=1)

        notifier = Notify()

        if obj.flag == False:

            notifier.start()
            obj.flag = True
            obj.save()
            return JsonResponse({'success': 'started'})

        else:

            notifier.stop()
            del notifier
            obj.delete()
            return JsonResponse({'success': 'stopped'})
