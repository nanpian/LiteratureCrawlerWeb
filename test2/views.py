#coding:utf-8
from django import template
from django import forms
from django.http import HttpResponse,Http404
from django.shortcuts import render,render_to_response
from django.template import Context,loader
from django.views.generic import View,TemplateView,ListView,DetailView
from django.db.models import Q
from django.core.cache import caches
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from blog.models import Article,Category,Carousel,Column,Nav,News
from vmaig_comments.models import Comment
from vmaig_auth.models import VmaigUser
from vmaig_auth.forms import VmaigUserCreationForm,VmaigPasswordRestForm
from vmaig_blog.settings import PAGE_NUM
import datetime,time
import json
import logging
from django.views.generic import TemplateView
from test2.models import  BlogsPost


#缓存
try:
    cache = caches['memcache']
except ImportError as e:
    cache = caches['default']

#logger
logger = logging.getLogger(__name__)
class TestView(TemplateView):
    template_name = "test2/test2.html"


class Test2View(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class TestView2(ListView):
    context_object_name = 'articleList'
    template_name = 'test2/test2.html'
    paginate_by = 50
    #model = ServerList
    http_method_names = [u'get',]

    def get_queryset(self):
        articleList = BlogsPost.objects.all()
        # plat = self.request.GET.get('plat')
        # keyword = self.request.GET.get('keyword')
        # if plat:
        #     serverlist = serverlist.filter(plat=plat)
        # if keyword:
        #     serverlist = serverlist.filter(Q(dx_ip=keyword)|Q(lt_ip=keyword)|Q(domain=keyword))
        return articleList

    def get_context_data(self, **kwargs):
        context = super(TestView2,self).get_context_data(**kwargs)
        # platlist = ServerList.objects.values('plat').annotate()
        # context['platlist'] = platlist
        return context