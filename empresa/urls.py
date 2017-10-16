from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_new, name='post_new'),
    url(r'^clasificacion/', views.clasificacion, name='clasificacion'),
    url(r'^eliminar/', views.eliminar, name='eliminar'),
]
