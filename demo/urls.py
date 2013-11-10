from django.conf.urls import patterns, include, url

from demo.views import DemoCarView, DemoCarViewPreload, DemoCarsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reverse_forward_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cars/$', DemoCarsView.as_view(), name='cars'),
    url(r'^car/(?P<pk>\d+)/$', DemoCarView.as_view(), name='car_detail'),
    url(r'^carpreload/(?P<pk>\d+)/$', DemoCarViewPreload.as_view(), name='car_detail_preload'),
)
