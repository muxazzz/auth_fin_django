from django.contrib import admin
from common.models import UserProfile  
  
# Register your models here.  
@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass
# Register your models here.
