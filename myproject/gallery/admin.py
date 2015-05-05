from django.contrib import admin

# Register your models here.

from gallery.models import TestModel
 
class TestModelAdmin(admin.ModelAdmin):
    list_filter = ('the_file','create_time')
    list_display = ('the_file','create_time')

admin.site.register(TestModel,TestModelAdmin)

