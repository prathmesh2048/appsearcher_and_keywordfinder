from django.contrib import admin
from .models import Keywords, Url
# Register your models here.


admin.site.register(Url)
admin.site.register(Keywords)