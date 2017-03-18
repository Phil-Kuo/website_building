# allow you to map URLs for your application


from django.conf.urls import patterns, url

#provide you with access to your views in "rango" 
from rango import views

#allow you to reference the view in the URL mapping 
urlpatterns = patterns('', url(r'^$'), views.index, name='index') #'^$ matches to an empty string'
