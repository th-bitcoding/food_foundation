from django.contrib import admin
from customeuser.models import CustomeUser
# Register your models here.
@admin.register(CustomeUser)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','id','user_type','is_active')