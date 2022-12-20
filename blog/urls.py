from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import all_blogs, post

urlpatterns = [
    path('', all_blogs, name='all blogs'),
    path('<str:post_title>', post),
]
