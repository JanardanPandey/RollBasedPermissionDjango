from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from rbpApp.models import SkylusUser

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class SkylusUserInline(admin.StackedInline):
#     model = SkylusUser
#     can_delete = False
#     verbose_name_plural = 'SkylusUser'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (SkylusUserInline,)

# # Re-register UserAdmin
# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import SkylusUser

# admin.site.register(SkylusUser, UserAdmin)