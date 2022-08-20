from django.urls import path

from shopping_list.api.views import ListAddShoppingList, ShoppingListDetail

urlpatterns = [
    path(
        "api/shopping-lists/", ListAddShoppingList.as_view(), name="all_shopping_lists"
    ),
    path(
        "api/shopping-lists/<uuid:pk>/",
        ShoppingListDetail.as_view(),
        name="shopping_list_detail",
    ),
]
