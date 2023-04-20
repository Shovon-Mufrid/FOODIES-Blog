from django.urls import path
from . import views

app_name = 'Blog_App'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('blogs/', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<slug>/', views.UpdateBlog.as_view(), name='edit_blog'),

]