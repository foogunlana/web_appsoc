from django.conf.urls import patterns,url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'forum.views.home', name='home'),
    url(r'^post$', 'forum.views.post', name='post'),
    url(r'^post/detail/(?P<pk>[0-9]+)/$', 'forum.views.detail', name='post_detail'),
    url(r'^post/like/(?P<pk>[0-9]+)/$', 'forum.views.like', name='like_post'),
    url(r'^post/unlike/(?P<pk>[0-9]+)/$', 'forum.views.unlike', name='unlike_post'),
    url(r'^post/sort/(?P<sort>[a-zA-Z0-9]+)/$', 'forum.views.sort', name='sort_posts'),
    url(r'^post/user/(?P<sort>[a-zA-Z0-9]+)/$', 'forum.views.sort_user', name='sort_user'),
    url(r'^comment$', 'forum.views.comment', name='comment'),
    # url(r'^blog/', include('blog.urls')),

)

urlpatterns += staticfiles_urlpatterns()
