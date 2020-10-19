from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','realtor','price','list_date','is_published')
    list_display_links = ('title','realtor')
    list_filter= ('realtor',)
    list_per_page = (3)
    list_editable = ('is_published',)
    # search_fields = ('title','state','city','realtor')
    search_fields = ['title',]


admin.site.register(Listing,ListingAdmin)



# Register your models here.
