from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'coalheartcache.views.home', name='home'),
    url(r'^personal/$', 'coalheartcache.views.personal', name='personal'),
    url(r'^personal/changename/$', 'coalheartcache.views.change_name', name='change_name'),
    url(r'^personal/changepass/$', 'coalheartcache.views.change_password', name='change_password'),
    url(r'^people/$', 'coalheartcache.views.main_page', name='main_page'),
    url(r'^people/(?P<name>\w+)/$', 'coalheartcache.views.category_list', name='category_list'),
    url(r'^story/(?P<name>\w+)/$', 'coalheartcache.views.story', name='story'),
    url(r'^story/(?P<name>\w+)/donate/$', 'coalheartcache.views.donate', name='donate'),
    url(r'^charity/$', 'coalheartcache.views.charity_list', name='charity_list'),
    url(r'^charity/(?P<name>\w+)/$', 'coalheartcache.views.charity', name='charity'),
    url(r'^register/$', 'coalheartcache.views.register', name='register'),
    url(r'^login/$', 'coalheartcache.views.login_view', name='login'),
    url(r'^logout/$', 'coalheartcache.views.logout_view', name='logout'),
)