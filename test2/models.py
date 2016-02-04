from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    summary = models.TextField(max_length=100,blank=True,null=True,verbose_name=u'摘要')
    content = models.TextField(blank=True,null=True,verbose_name=u'内容')
    author = models.CharField(max_length=100,verbose_name=u'作者')
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return '%s' % (self.title)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            import datetime
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','summary')

admin.site.register(BlogsPost,BlogPostAdmin)