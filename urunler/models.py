from django.db import models
from django.utils.text import slugify

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=15)

    def __str__(self):
        return self.isim

class AltKategori(models.Model):
    isim = models.CharField(max_length=15)

    def __str__(self):
        return self.isim

class Urun(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    altKategori = models.ManyToManyField(AltKategori)
    marka = models.CharField(max_length=30)
    urunAciklama = models.TextField(max_length=200)
    eskiFiyat = models.IntegerField()
    indirimliFiyat = models.IntegerField()
    urunResmi = models.FileField(upload_to='urunler/', blank=True, null=True)
    slug = models.SlugField(null=True,blank=True, editable=False)
    
    def __str__(self):
        return self.urunAciklama
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.urunAciklama)
        super().save(*args, **kwargs)