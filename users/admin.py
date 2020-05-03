from django.contrib import admin
from django.contrib.admin import TabularInline
from menus.models import Menu
from users.models import User, Company


class MenuInline(TabularInline):
    fk_name = 'company'
    model = Menu
    readonly_fields = ['name', 'date_modified', 'date_created']
    fields = ['name', 'description', 'company', 'date_modified', 'date_created']
    can_delete = False
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "current_menu":
            if not request.user.is_superuser:
                kwargs["queryset"] = Menu.objects.filter(company=request.user.company)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()

        if not request.user.is_superuser:
            qs = qs.filter(id=request.user.company.id)

        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


    model = Company
    readonly_fields = ['date_modified', 'date_created']
    fields = ['name', 'current_menu', 'date_modified', 'date_created']
    list_display = ['name', ]
    inlines = [
        MenuInline,
    ]


admin.site.register(User)
admin.site.register(Company, CompanyAdmin)
