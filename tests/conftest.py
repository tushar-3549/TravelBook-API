import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nol_backend.settings.local")
django.setup()

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username="toma", email="toma@gmail.com", password="toma123")

@pytest.fixture
def auth_client(api_client, user):
    # JWT register/login না ধরলে, সরাসরি force_authenticate করে টেস্ট করা যায়
    api_client.force_authenticate(user=user)
    return api_client

