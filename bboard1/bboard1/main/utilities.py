from django.template.loader import render_to_string
# from bboard1.bboard1.settings import ALLOWED_HOSTS # n
from django.core.signing import Signer
from datetime import datetime
from os.path import splitext
# import sys
# sys.path.append("..")

import sys
from pprint import pprint
sys.path.append("/home/Python_Projects/bboard1")
pprint(sys.path)



# import bboard1.bboard1.settings

# import settings # n
# from settings import ALLOWED_HOSTS # n
# from bboard1.settings import ALLOWED_HOSTS # n # No module named 'bboard1.bboard1' # n
# from bboard1.bboard1.settings import ALLOWED_HOSTS # n



signer = Signer()

def send_activation_notification(user):
    #----------------------inserted----------------------------------
    ALLOWED_HOSTS = []
    # ----------------------endinserted----------------------------------
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {
        'user': user,
        'host': host,
        'sign': signer.sign(user.username)
    }
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(),splitext(filename)[1])
