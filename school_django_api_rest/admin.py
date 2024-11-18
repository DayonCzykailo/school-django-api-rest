from django.contrib import admin
from school_django_api_rest.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'phone')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'cpf', 'phone')
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code', 'description')
    search_fields = ('code', 'description', 'level')
    list_per_page = 20 

admin.site.register(Course, Courses)