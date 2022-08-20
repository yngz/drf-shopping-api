from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from shopping_list.api.serializers import ShoppingItemSerializer
from shopping_list.models import ShoppingItem


class ShoppingItemViewSet(ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    @action(
        detail=False,
        methods=["DELETE"],
    )
    def delete_purchased(self, request):
        ShoppingItem.objects.filter(purchased=True).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
