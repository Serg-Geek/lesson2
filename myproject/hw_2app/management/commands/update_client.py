from django.core.management.base import  BaseCommand
from hw_2app.models import Client

class Command(BaseCommand):
    help = "update client"

    def update_client(self, client_id, name, email, phone_number, address, registration_date):
        client = Client.objects.get(pk=client_id)
        client.name = name
        client.email = email
        client.phone_number = phone_number
        client.address = address
        client.registration_date = registration_date
        client.save()

