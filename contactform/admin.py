from django.contrib import admin

# Register your models here.
from contactform.models import Contactform
class ContactAdmin(admin.ModelAdmin):
    list_display=('fullname','email','subject','message')
admin.site.register(Contactform,ContactAdmin)
