from django_mongoengine import mongo_admin as admin
from .models import MongoUser


class UserAdmin(admin.DocumentAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    list_display = ["username", "email", "date_joined", ]


admin.site.register(MongoUser, UserAdmin)
