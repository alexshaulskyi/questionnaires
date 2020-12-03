import threading
from datetime import datetime, date
import time

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

from users.models import User
from tests.models import UserPassedTest


def worker():

    while True:

        now = datetime.now().strftime("%H:%M:%S")

        window_starts = '04:57:00'
        window_ends = '04:57:30'

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

thread = threading.Thread(target=worker)
thread.start()
