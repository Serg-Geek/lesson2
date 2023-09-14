from django.core.management.base import  BaseCommand
from hw_2app.models import Client

class Command(BaseCommand):
    help = "Create client"



    def create_client(name, email, phone_number, address, registration_date):
        client = Client(name=name, email=email, phone_number=phone_number, address=address, registration_date=registration_date)
        client.save()
