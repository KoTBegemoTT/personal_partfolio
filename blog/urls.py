from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import all_blogs, post

app_name = 'blog'

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('<str:post_title>', post),
]
