from django.contrib import admin
from .models import fb_form
# Register your models here.
class fb_formAdmin(admin.ModelAdmin):
    list_display = ('c_name','date','outof')
    list_filter = ('outof','date')

    class Meta:
        model=fb_form


admin.site.register(fb_form, fb_formAdmin)