from django.contrib import admin

from .models import Realtor

class Realtoradmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date')
    list_display_links=('name','email')
    search_fields = ('name',)
    list_per_page = 10



admin.site.register(Realtor,Realtoradmin)
# Register your models here.
