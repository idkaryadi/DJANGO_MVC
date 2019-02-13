from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('post_new/', views.input_post, name='post_new'),
    path('post/<int:post_id>/', views.post_detail, name = 'post_detail'),
]