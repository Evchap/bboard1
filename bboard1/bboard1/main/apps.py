from django.apps import AppConfig
from django.dispatch import Signal

from .utilities import send_activation_notification

class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Доска объявлений'

# user_registered = Signal(providing_args=['instance'])
    # TypeError: Signal.__init__() got an unexpected keyword argument 'providing_args'
    # providing_args - устарело
user_registered = Signal('instance') # новый вариант
# user_registered = Signal() # новый вариант

def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registered.connect(user_registered_dispatcher)