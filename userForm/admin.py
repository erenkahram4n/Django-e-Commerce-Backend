from django.contrib import admin
from .models import Contact

class ContactBaslik(admin.ModelAdmin):
    list_display = ('email','name','username')
    list_filter = ('email','name','username')
    search_fields = ('email','name','username')
    readonly_fields = ('email','name','username','text')

# Register your models here.

admin.site.register(Contact, ContactBaslik)