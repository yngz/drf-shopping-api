from django.contrib.auth.models import User
from rest_framework import serializers
from shopping_list.models import ShoppingItem, ShoppingList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]
        read_only_fields = ("id",)

    def create(self, validated_data, **kwargs):
        shopping_list_id = self.context["request"].parser_context["kwargs"]["pk"]
        if ShoppingList.objects.get(id=shopping_list_id).shopping_items.filter(
            name=validated_data["name"], purchased=False
        ):
            raise serializers.ValidationError("Item already exists on the list.")

        validated_data["shopping_list_id"] = shopping_list_id

        return super(ShoppingItemSerializer, self).create(validated_data)


class ShoppingListSerializer(serializers.ModelSerializer):
    unpurchased_items = serializers.SerializerMethodField()
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ["id", "name", "unpurchased_items", "members"]

    def get_unpurchased_items(self, obj):
        return [
            {"name": shopping_item.name}
            for shopping_item in obj.shopping_items.filter(purchased=False)
        ][:3]
