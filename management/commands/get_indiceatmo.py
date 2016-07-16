from django.core.management.base import BaseCommand, CommandError
from atmogwada.models import IndiceAtmo

from atmo.atmo import Atmo

class Command(BaseCommand):
    help = 'Retrieves indice atmo and forecast and store it in the database '
    'if data changed since last record.'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        ia = Atmo()
        current_atmo = IndiceAtmo(config_date=ia.indiceatmo['config_date'],
                                  date_today=ia.indiceatmo['date_today'],
                                  tomorrow=int(ia.indiceatmo['tomorrow']),
                                  today=int(ia.indiceatmo['today']))
        last_atmo = IndiceAtmo.objects.last()

        if current_atmo.config_date != last_atmo.config_date \
                or current_atmo.date_today != last_atmo.date_today \
                or current_atmo.tomorrow != last_atmo.tomorrow \
                or current_atmo.today != last_atmo.today:
            current_atmo.save()
