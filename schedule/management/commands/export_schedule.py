from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Export production schedule as fixtures'

    def handle(self, *args, **options):
        # Dump production schedule as fixtures
        call_command('dumpdata', 'schedule.ProductionSchedule', '--natural-foreign', '--natural-primary', '--indent',
                     '4', '--output', 'schedule/fixtures/production_schedule.json')
