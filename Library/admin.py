from django.contrib import admin
from .models import Books,Authors
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','name','genre')
    search_fields = ['name','id','genre',]

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'genre')
    search_fields = ['name', 'id','genre','year','country']
admin.site.register(Books,BooksAdmin)
admin.site.register(Authors,AuthorsAdmin)