from django.contrib import admin
from hoardingusers.models import UserType, UserInfo


# Admin Views
class UserTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'created', 'enabled', 'comment',)
    
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'posts', 'updated', 'comment',)
    

# Added to Admin View
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserInfo, UserInfoAdmin)