from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext_lazy as _
from environ import Env
from apps.store.admin import ProductAdmin
from apps.store.models import Product
from apps.tags.models import TaggedItem
from apps.core.models import User


env = Env()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ["tag"]


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


# admin.site.unregister(Product)
# admin.site.register(Product, CustomProductAdmin)


admin.site.site_title = _(env("APP_TITLE", cast=str))
admin.site.site_header = _(env("APP_TITLE", cast=str))
admin.site.index_title = _(env("INDEX_TITLE", cast=str))
