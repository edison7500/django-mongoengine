from django_mongoengine import mongo_admin as admin
from .models import MongoUser


class UserAdmin(admin.DocumentAdmin):
    pass


admin.site.register(MongoUser, UserAdmin)
