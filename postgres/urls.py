"""postgres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]


from django.conf.urls import url, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(router.urls)),        
    url(r'sector_index', views.sector_index, name='sector_index'),
    url(r'begin_page_2', views.begin_page_2, name='begin_page_2'),
    url(r'grading', views.grading, name='grading'),    
    url(r'effect_page', views.effect_page, name='effect_page'),   
    url(r'result_page', views.result_page, name='result_page'),     
    # url(r'^', views.sector_index, name='sector_index'),       
    # url(r'^(?P<sector>[-\w]+)/$', views.base, name='heads')
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
