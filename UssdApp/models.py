from django.db import models


class UssdUser(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    session_id = models.CharField(max_length=50)
    service_code = models.CharField(max_length=12)
    language = models.CharField(max_length=5)
    ussd_input = models.CharField(max_length=10)

    @staticmethod
    def add(data):
        print('******data = ', data)
        entry = UssdUser(
            phone_number=data['phone_number'],
            session_id=data['session_id'],
            service_code=data['service_code'],
            language=data['language'],
            ussd_input=data['ussd_input']
        )
        entry.save()


class EntryError(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    session_id = models.CharField(max_length=50)
    service_code = models.CharField(max_length=12)
    language = models.CharField(max_length=5)
    ussd_input = models.CharField(max_length=10)
    wrong_entry = models.CharField(max_length=10, blank=True)

    @staticmethod
    def add(data, wrong_entry):
        entry = EntryError(
            phone_number=data.phone_number,
            session_id=data.session_id,
            service_code=data.service_code,
            language=data.language,
            ussd_input=data.ussd_input,
            wrong_entry=wrong_entry
        )
        entry.save()
