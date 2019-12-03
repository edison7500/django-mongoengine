from django_mongoengine import mongo_admin as admin
from .models import MongoUser


class UserAdmin(admin.DocumentAdmin):
    list_display = ["username", "email", ]


admin.site.register(MongoUser, UserAdmin)
