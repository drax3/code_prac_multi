from django.contrib import admin
from animals.models import Cat

# Register your models here.
class CatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cat, CatsAdmin)