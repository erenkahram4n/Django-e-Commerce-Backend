from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(marka__icontains = search) |
            Q(urunAciklama__icontains = search) |
            Q(kategori__isim__icontains = search) |
            Q(altKategori__isim__icontains = search)
        )
    context = {
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler
    }
    return render(request, 'index.html',context)
def form(request):
    return render(request, 'form.html')
def sepet(request):
    return render(request, 'sepet.html')
def urunDetail(request,urunId):
    urun = Urun.objects.filter(slug = urunId)
    context = {
        'urun':urun
    }
    return render(request, 'urun.html',context)
def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Ürün Başarıyla Yüklendi!')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

def view_404(request, exception):
    return redirect('/')