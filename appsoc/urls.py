from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from appsoc import views


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.events, name='events'),
                       url(r'^home/$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^hub/$', views.github, name='github'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^register/(?P<success>[a-zA-Z]+)/$',
                           views.register, name='register_success'),
                       url(r'^login/$', views.login_view, name='login_view'),
                       url(r'^logout/$', views.logout_view,
                           name='logout_view'),
                       url(r'^bank/$', views.bank, name='bank'),
                       url(r'^learn/$', views.learn, name='learn'),
                       url(r'^events/$',
                           views.events, name='events'),
                       url(r'^events/(?P<success>[a-zA-Z]+)/$',
                           views.events, name='events_success'),
                       )


urlpatterns += staticfiles_urlpatterns()
