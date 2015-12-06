from django.conf.urls import patterns, url
from django.contrib.auth.forms import UserCreationForm
from apps.threads.views import (
LinkListView, logout_view, auth, subreddit_view, subreddit_selector,
link_discuss, submit_link, register
)

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^auth/$', auth, name='auth'),
    url(r'^submit_link/$', submit_link, name='submit_link'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^r/$', subreddit_view, name='subreddits'),
    url(r'^r/(?P<sub>[\w]+)/$', subreddit_selector, name='subreddits'),
    url(r'^discuss/(?P<link>[\w-]+)/$', link_discuss, name='links'),
)
