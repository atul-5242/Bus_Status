from django.contrib import admin
from signup_student.models import StudentDetails

class ServiceAdmin(admin.ModelAdmin):
    list_display=('email','Id','password1','password2')
    
admin.site.register(StudentDetails,ServiceAdmin)
# Register your models here.
