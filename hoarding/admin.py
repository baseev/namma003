from django.contrib import admin
from hoarding.models import Hoarding, HoardingType, MediaType

# Admin Views
class HoardingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'town': ('town',)}
    list_display = ('town', 'user', 'media_type', 'created', 'enabled', 'comment',)
    

    

# Added to Admin View
admin.site.register(Hoarding, HoardingAdmin)
admin.site.register(HoardingType)
admin.site.register(MediaType)
