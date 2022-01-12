from django.contrib import admin

# Register your models here.
from polls.models import Category, QuesModel



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name'] 

class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'ans']


admin.site.register(Category, CategoryAdmin)
admin.site.register(QuesModel, QuesModelAdmin)