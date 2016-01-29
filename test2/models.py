from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    summary = models.TextField(max_length=100,blank=True,null=True,verbose_name=u'摘要')
    content = models.TextField(blank=True,null=True,verbose_name=u'内容')
    author = models.CharField(max_length=100,verbose_name=u'作者')
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','summary')

admin.site.register(BlogsPost,BlogPostAdmin)