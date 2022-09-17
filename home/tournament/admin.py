from django.contrib import admin
from .models import stadium, team, player

# Register your models here.

#registros de los modelos
admin.site.register(stadium)
admin.site.register(team)
admin.site.register(player)