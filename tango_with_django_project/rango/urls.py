# allow you to map URLs for your application


from django.conf.urls import patterns, url

#provide you with access to your views in "rango" 
from rango import views

#allow you to reference the view in the URL mapping 
urlpatterns = patterns('', 
    url(r'^$', views.index, name='index') ,
    #url(r'^about/$', views.about, name = 'about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name = 'category'),)#'^$' matches to an empty string'
