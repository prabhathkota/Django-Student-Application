from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StudentWebsite.views.home', name='home'),
    # url(r'^StudentWebsite/', include('StudentWebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('StudentWebsite.StudentApp.views',
	#url(r'^$', 'home'),
	url(r'^home/$', 'subjectView', name="home"),
    url(r'^getMarksDetailsView/(?P<subjectName>\w+)/$', 'getMarksDetailsView', name="getMarksDetailsView"),
)