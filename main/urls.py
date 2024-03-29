from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='eng'),
    path('rus', russian_mode, name='rus'),
    path('kaz', kazakh_mode, name='kaz')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)