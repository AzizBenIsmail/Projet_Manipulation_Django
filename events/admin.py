from django.contrib import admin
from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    #pass
    list_display=('title','state','categorie')
    list_filter=('title','state','categorie')
    list_per_page=4
    ordering=('title','state','categorie')
    search_fields=['title','categorie']

admin.site.register(Event,EventAdmin)
