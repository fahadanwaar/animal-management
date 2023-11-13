from django.apps import AppConfig
from django.core.management import call_command

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        call_command('migrate',
                     app_label='api',
                     verbosity=1,
                     interactive=False,
                     database='memory')
