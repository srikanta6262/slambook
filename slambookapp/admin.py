from django.contrib import admin
from slambookapp.models import Fillup

# Register your models here.
class FillupAdmin(admin.ModelAdmin):
    list_display=['Firstname','Lastname','gender','phone','add']

admin.site.register(Fillup,FillupAdmin)
