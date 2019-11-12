from django.contrib import admin
from . models import  Movie
from . models import  Hour
from . models import  Room
from . models import  Client
from . models import  Session
admin.site.register(Movie)
admin.site.register(Hour)
admin.site.register(Room)
admin.site.register(Client)
admin.site.register(Session)