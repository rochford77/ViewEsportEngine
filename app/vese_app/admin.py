from django.contrib import admin

from .models import *

admin.site.register(Player)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Season)
admin.site.register(Week)
admin.site.register(Series)
admin.site.register(Game)

# Register your models here.
