from django.contrib import admin # Register your models here.
from cars.models import Car,Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ['model','brand', 'factroy_year', 'model_year', 'price','photo'] 
    search_fields = ('model','brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)

admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)