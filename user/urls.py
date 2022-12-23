
from django.urls import path
from user.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('kayit/', userRegister, name='register'),
    path('giris/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)