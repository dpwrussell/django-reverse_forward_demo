from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reverse_forward_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^demo/', include('demo.urls')),
)
