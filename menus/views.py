from django.db.models import QuerySet, Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Menu, Dish
from .serializers import DishSerializer, MenuSerializer


class DishViewset(ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class MenuViewset(ReadOnlyModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    # Define sorting:
    sortable_fields = ('name', )
    custom_sorting = {
        'dish_count': lambda queryset, order_by: queryset.annotate(dish_count=Count('dishes')).order_by(order_by)
    }

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        # TODO: remove prints in production. Left only for convenience of reviewer.
        if (order_by := self.request.query_params.get('orderring', '').lower()).lstrip('-') in self.sortable_fields:
            # print(f'Orderred by {order_by}')
            queryset = self.queryset.order_by(order_by)
        elif order_by.lstrip('-') in self.custom_sorting.keys():
            # print(f'Orderred by {order_by}')
            queryset = self.custom_sorting[order_by.lstrip('-')](self.queryset, order_by)
        else:
            # print(f'Orderred by ID')
            queryset = self.queryset.order_by('id')

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset
