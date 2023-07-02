from django.core.management.base import BaseCommand
from django.core.management import call_command

from django.conf import settings

class Command(BaseCommand):
    help = 'Migrates all databases'

    def handle(self, *args, **options):
        databases = list(settings.DATABASES.keys())
        for database in databases:
            call_command('migrate', database=database)
