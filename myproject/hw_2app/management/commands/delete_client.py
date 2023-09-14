from django.core.management.base import  BaseCommand
from hw_2app.models import Client

class Command(BaseCommand):
    help = "delete client"

    def delete_client(client_id):
        client = Client.objects.get(pk=client_id)
        client.delete()

