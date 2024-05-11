from django.contrib import admin
from .models import UserInfo  # Import your model

class UserInfoAdmin(admin.ModelAdmin):
  list_display = ['id','membership_id', 'fname', 'lname', 'gender', 'dob', 'address', 'city', 'state', 'country', 'zip_code', 'phone', 'email']
# Register the model with the custom admin class
admin.site.register(UserInfo, UserInfoAdmin)
