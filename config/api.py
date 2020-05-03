from rest_framework import routers
from menus import views as menu_views

router = routers.DefaultRouter()
router.register('menus', menu_views.MenuViewset)
router.register('dishes', menu_views.DishViewset)
