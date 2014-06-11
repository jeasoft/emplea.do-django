from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from core.views import JobList, JobDetail, JobCreate
from core.api import JobResource

v1_api = Api(api_name='v1')
v1_api.register(JobResource())

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emplea_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', JobList.as_view()),
    url(r'^job/new/$', JobCreate.as_view()),
    url(r'^job/(?P<pk>\d+)/$', JobDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/', include(v1_api.urls)),
)
