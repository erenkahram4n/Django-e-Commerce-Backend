from django.forms import ModelForm
from .models import *
from builtins import *

class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['kategori', 'altKategori', 'urunAciklama','marka','eskiFiyat','indirimliFiyat','urunResmi']

    def __init__(self, *args, **kwargs):
        super(UrunForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})