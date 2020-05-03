from django.contrib import admin
from django.contrib.admin import TabularInline
from menus.models import Dish, Menu


class DishInline(TabularInline):
    model = Menu.dishes.through
    can_delete = False
    extra = 0


class MenuAdmin(admin.ModelAdmin):

    model = Menu
    readonly_fields = ['company', 'date_modified', 'date_created']
    fields = ['company', 'name', 'description', 'date_modified', 'date_created']
    list_per_page = 20
    inlines = [
        DishInline
    ]

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()

        if not request.user.is_superuser:
            qs = qs.filter(company=request.user.company)

        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        obj.company = request.user.company
        super(MenuAdmin, self).save_model(request, obj, form, change)


class DishAdmin(admin.ModelAdmin):

    model = Dish
    readonly_fields = ['company', 'image_tag', 'date_modified', 'date_created']
    fields = ['company', 'name', 'image_tag', 'description', 'image', 'price', 'preparation_time', 'is_vegan', 'date_modified', 'date_created']
    list_display = ['name', 'price', 'is_vegan', 'date_modified', 'date_created']
    list_per_page = 20

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "menus":
            if not request.user.is_superuser:
                kwargs["queryset"] = Menu.objects.filter(company=request.user.company)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.company = request.user.company
        super(DishAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()

        if not request.user.is_superuser:
            qs = qs.filter(company=request.user.company)

        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


admin.site.register(Dish, DishAdmin)
admin.site.register(Menu, MenuAdmin)
