# encoding:utf8

from django.conf.urls import url
from views import UserList, GroupList

app_name = 'snippets'
urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^groups/$', GroupList.as_view()),
]
