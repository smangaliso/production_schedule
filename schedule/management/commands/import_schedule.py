import csv
from django.core.management.base import BaseCommand
from schedule.models import ProductionSchedule, Machine, Event
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Import a production schedule from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        filename = options['filename']

        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    machine, _ = Machine.objects.get_or_create(
                        name=row['machine_name'].strip(),
                        serial_number=row['machine_serial_number'].strip()
                    )
                    event, _ = Event.objects.get_or_create(
                        event_name=row['event_name'].strip(),
                        event_code=row['event_code'].strip()
                    )

                    start_time = timezone.make_aware(datetime.strptime(row['start_time'].strip(), '%Y-%m-%d %H:%M:%S'),
                                                     timezone.get_default_timezone())

                    if 'duration' in row:
                        duration = int(row['duration'].strip())
                        end_time = start_time + timezone.timedelta(minutes=duration)
                    else:
                        end_time = timezone.make_aware(datetime.strptime(row['end_time'].strip(), '%Y-%m-%d %H:%M:%S'),
                                                       timezone.get_default_timezone())

                    ProductionSchedule.objects.create(
                        machine=machine,
                        event=event,
                        start_time=start_time,
                        end_time=end_time
                    )

                except KeyError as e:
                    self.stdout.write(self.style.ERROR(f'Error: missing field "{e.args[0]}" in CSV row'))
                    continue
                except ValueError as e:
                    self.stdout.write(self.style.ERROR(f'Error: invalid value "{e.args[0]}" in CSV row'))
                    continue

