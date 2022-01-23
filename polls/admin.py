import site
from django.contrib import admin

# Register your models here.
from polls.models import Category, QuesModel, UserProfile



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status'] 



class QuesModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'ans']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city', 'email']


admin.site.register(Category, CategoryAdmin)
admin.site.register(QuesModel, QuesModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)