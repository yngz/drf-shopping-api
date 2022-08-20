import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from shopping_list.models import ShoppingItem, ShoppingList


@pytest.mark.django_db
def test_valid_shopping_list_is_created():
    url = reverse("all-shopping-lists")
    data = {
        "name": "Groceries",
    }
    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert ShoppingList.objects.get().name == "Groceries"


def test_shopping_list_name_missing_returns_bad_request():
    url = reverse("all-shopping-lists")
    data = {"something_else": "blahblah"}
    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
