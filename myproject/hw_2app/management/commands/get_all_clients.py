from django.core.management.base import  BaseCommand
from hw_2app.models import Client

class Command(BaseCommand):
    help = "get_all_clients"

    def get_all_clients(self):
        clients = Client.objects.all()
        return clients

