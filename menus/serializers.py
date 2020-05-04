from rest_framework import serializers
from .models import Menu, Dish


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Menu
        fields = ('id', 'company_name', 'dish_count', 'name', 'description', 'dishes', 'date_modified', 'date_created')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'menus', 'description', 'price', 'preparation_time', 'is_vegan', 'date_modified',
                  'date_created')
