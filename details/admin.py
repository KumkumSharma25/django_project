from django.contrib import admin
from details.models import Dynamic
# Register your models here.
class DynamicAdmin(admin.ModelAdmin):
    list_display=('dynamic_title','dynamic_desc','dynamic_img_link','dynamic_read_link','dynamic_imgg')
admin.site.register(Dynamic,DynamicAdmin)    
