from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers
from myapp import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'station', views.StationViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','myapp.views.home'),
    url(r'^index/','myapp.views.index'),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^login/','myapp.views.login_user'),
    # Examples:
    # url(r'^$', 'RestAPITemp.views.home', name='home'),
    # url(r'^RestAPITemp/', include('RestAPITemp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
