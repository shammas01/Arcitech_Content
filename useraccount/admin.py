from django.contrib import admin
from . models import (
    User,
    Content,
    Category
)
# Register your models here.

admin.site.register(User)
admin.site.register(Content)
admin.site.register(Category)