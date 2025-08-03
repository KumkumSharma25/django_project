from django.contrib import admin
from .models import House, Room

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'furniture',)


# Register your models here.
