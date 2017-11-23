from django.conf.urls import url
from . import views
app_name='search'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^abc$', views.resp,name='resp'),
]
