from rest_framework import routers
from menus import views as menu_views
from users import views as user_views

router = routers.DefaultRouter()
router.register('menus', menu_views.MenuViewset)
router.register('dishes', menu_views.DishViewset)
router.register('companies', user_views.CompanyViewSet)
