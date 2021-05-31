import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:signup")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:menu")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:login")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:about")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_root_url(client):
    url = reverse("store:gallery")
    response = client.get(url)
    assert response.status_code == 200