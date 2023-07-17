from django.contrib import admin

from .models import *

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_image')

class PublicationImageAdmin(admin.ModelAdmin):
    list_display = ('publication', 'image')

class PublicationVideoAdmin(admin.ModelAdmin):
    list_display = ('publication', 'video')

class ClergymanAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'job_title')

class ParishAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_image', 'address')

class ParishImageAdmin(admin.ModelAdmin):
    list_display = ('parish', 'image')

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('date', 'saints', 'day_parable')

class PhotogalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Clergyman, ClergymanAdmin)
admin.site.register(Parish, ParishAdmin)
admin.site.register(ParishImage, ParishImageAdmin)
admin.site.register(PublicationImage, PublicationImageAdmin)
admin.site.register(PublicationVideo, PublicationVideoAdmin)
admin.site.register(Calendar, CalendarAdmin) 
admin.site.register(Photogallery, PhotogalleryAdmin) 