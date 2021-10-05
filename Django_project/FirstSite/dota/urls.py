from django.urls import path, re_path


from .views import *

urlpatterns = [
    path('', index,  name='home'),
    path('templates/dota/about/about.html', about, name='about'),
    path('templates/dota/Gallery/gallery.html', gallery, name='gallery'),
    path('templates/dota/ourteam/our.html', ourteam, name='ourteam'),
    path('templates/dota/index.html', logo, name='logo'),
    path("templates/dota/login/login.html", login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),

]