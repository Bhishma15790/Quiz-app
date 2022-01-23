
import email
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.fields import SlugField
from django.contrib.auth.models import User

# Create your models here.
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe
# Create your models here.



class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
   

    class MPTTMeta:
        order_insertion_by = ['name']


    


class QuesModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.user.username


    def user_name(self):
        return self.user.username + ' [' + self.user.username + '] '
