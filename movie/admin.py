from django.contrib import admin
from .models import *

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_pub', 'catagory',
                    'quality', 'add_date')
    list_filter = ('year', 'catagory', 'quality')
    search_fields = ('title', 'year', 'overview',
                     'collections', 'tmdb_id', 'imdb_id')
    list_per_page = 30


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'gender')
    search_fields = ('name', 'biography', 'tmdb_id', 'imdb_id')
    list_per_page = 30


class MojalossAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'path')
    list_per_page = 25


class NeedToDownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'url', "done")
    list_per_page = 30
    search_fields = ('title', 'year', 'url')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Year)
admin.site.register(Movie_Category)
admin.site.register(Qualitie)
admin.site.register(Genre)
admin.site.register(Trailer)
admin.site.register(Collection)
admin.site.register(Actor)
admin.site.register(Movie_actor_name)
admin.site.register(Mojaloss, MojalossAdmin)
# This one for mojaloss direct link given movies
admin.site.register(NeedToDownload, NeedToDownloadAdmin)
