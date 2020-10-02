import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django

django.setup()
from django.contrib.auth.models import Group

GROUPS = ['admin','anonymous','user','org_admin']
MODELS = ['user']

for group in GROUPS:
    created_group = Group.objects.get_or_create(name=group)