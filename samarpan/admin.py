from django.contrib import admin
from .models import Students,Institutions

# Register your models here.
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'institution_type', 'city', 'email')
    search_fields = ['institution_name', 'city', 'email']
    list_filter = ['institution_type', 'city']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'surname', 'mobile', 'email', 'institution', 'blood_group', 'gender')
    list_filter = ('institution', 'blood_group', 'gender', 'year', 'stream')

# Register your models with the admin site
admin.site.register(Institutions, InstitutionAdmin)
admin.site.register(Students, StudentAdmin)
