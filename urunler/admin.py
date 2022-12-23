from django.contrib import admin
from .models import *

class UrunBaslik(admin.ModelAdmin):
    list_display = ('marka','urunAciklama','slug','indirimliFiyat')
    list_filter = ('marka','urunAciklama','indirimliFiyat')
    search_fields = ('marka','urunAciklama')
    readonly_fields = ('slug','slug')

admin.site.register(Urun, UrunBaslik)
admin.site.register(Kategori)
admin.site.register(AltKategori)