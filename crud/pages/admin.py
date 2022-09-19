from django.contrib import admin
from .models import Player, Team, Stadium

# Register your models here.

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Stadium)