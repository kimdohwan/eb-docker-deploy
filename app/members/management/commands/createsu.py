import json
import os

# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from config.settings.base import SECRET_DIR

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        secrets = json.load(open(os.path.join(SECRET_DIR, 'base.json')))

        if not User.objects.filter(username=secrets['SUPERUSER_USERNAME']).exists():
            User.objects.create_superuser(
                username=secrets['SUPERUSER_USERNAME'],
                password=secrets['SUPERUSER_PASSWORD'],
                email=secrets['SUPERUSER_EMAIL'],
            )

