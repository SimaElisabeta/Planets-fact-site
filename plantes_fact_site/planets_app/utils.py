import os
from django.conf import settings


def get_api_key():
    filename = os.path.join(settings.BASE_DIR, 'static', 'secrets', 'api_key.txt')
    with open(filename, 'r') as f:
        key = f.read()
    return key
