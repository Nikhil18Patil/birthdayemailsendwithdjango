from django.core.management.base import BaseCommand
from datetime import date
import schedule
import time
from django.core.mail import send_mail
from birthdaywishes.models import Persons
from django.conf import settings

class Command(BaseCommand):
    help = 'Send birthday wishes via email to people with birthdays today'

    def send_birthday_wishes(self):
        today = date.today()
        people_with_birthday = Persons.objects.filter(birth_date__day=today.day, birth_date__month=today.month)

        for person in people_with_birthday:
            subject = 'Happy Birthday!'
            message = f'Hi {person.name},\n\nHappy Birthday! 🎉🎂'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [person.email]  # Assuming you have an 'email' field in your Persons model

            try:
                send_mail(subject, message, from_email, recipient_list)
                self.stdout.write(self.style.SUCCESS(f'Sent birthday wishes to {person.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to send birthday wishes to {person.name}: {str(e)}'))

    def handle(self, *args, **kwargs):
        # Schedule the task to run at 12:00 PM
        schedule.every().day.at("13:14").do(self.send_birthday_wishes)


        while True:
            schedule.run_pending()
            time.sleep(60)  # Sleep for 60 seconds
