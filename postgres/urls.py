
from django.conf.urls import url, include
from rest_framework import routers
from api import views
from django.contrib import admin


router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(router.urls)),    
    url(r'admin/', admin.site.urls),        
    url(r'sector_index', views.sector_index, name='sector_index'),
    url(r'begin_page_2', views.begin_page_2, name='begin_page_2'),
    url(r'grading', views.grading, name='grading'),    
    url(r'effect_page', views.effect_page, name='effect_page'),   
    url(r'result_page', views.result_page_new, name='result_page_2'),
    url(r'request_new_dev', views.request_new_dev, name='request_new_dev'),
    url(r'', views.sector_index, name='sector_index'),     
    # url(r'^', views.sector_index, name='sector_index'),       
    # url(r'^(?P<sector>[-\w]+)/$', views.base, name='heads')
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
