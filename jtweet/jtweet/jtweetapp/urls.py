from django.conf.urls import patterns, url

urlpatterns = patterns('jtweet.jtweetapp.views',
    # Examples:
    # url(r'^$', 'jtweet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^','index', name='index'),
)
