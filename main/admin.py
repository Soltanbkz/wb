from django.contrib import admin

from requests.models import Contact
from .models import *
from django.forms import Media
# Register your models here.


@admin.register(GeneralPage)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id','general_text', 'general_photo', 'date_created')
    list_filter = ('id','date_created', 'general_text')
    search_fields = ('id','date_created', 'general_text')


@admin.register(AboutText)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','about_text', 'about_photo', 'date_created')
    list_filter = ('id','date_created', 'about_text')
    search_fields = ('id','date_created', 'about_text')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'portfolio_text', 'port_img', 'port_text','date_created')
    list_filter = ('id','date_created', 'port_text', 'portfolio_text')
    search_fields = ('id','date_created', 'port_text', 'portfolio_text')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'name', 'email','text','date_created')
    list_filter = ('id','date_created', 'name', 'email')
    search_fields = ('id','date_created', 'name', 'email')

