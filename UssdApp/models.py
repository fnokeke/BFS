from django.db import models


class UssdLog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    session_id = models.CharField(max_length=50)
    service_code = models.CharField(max_length=12)
    language = models.CharField(max_length=5)
    screen_answered = models.CharField(max_length=30, default='')
    ussd_input = models.CharField(max_length=30)
    has_error = models.BooleanField(default=False)
    seconds_spent = models.IntegerField(default=0)
    next_screen = models.CharField(max_length=30, default='')

    class Meta:
        db_table = 'ussd_log'

    @staticmethod
    def add(data):
        entry = UssdLog(
            phone_number=data['phone_number'],
            session_id=data['session_id'],
            service_code=data['service_code'],
            language=data['language'],
            screen_answered=data['screen_answered'],
            ussd_input=data['ussd_input'],
            has_error=data['has_error'],
            seconds_spent=data['seconds_spent'],
            next_screen=data['next_screen']
        )
        entry.save()

