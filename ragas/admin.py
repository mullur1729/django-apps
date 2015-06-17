from django.contrib import admin

# Register your models here.
from .models import Raga, Thaat, FilmSong

admin.site.register(Raga)
admin.site.register(Thaat)
admin.site.register(FilmSong)
