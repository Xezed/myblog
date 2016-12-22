from django.conf.urls import url

from .views import DeleteList, CreateList, PostDetail, PostUpdate

urlpatterns = [
    url(r'^create/$', CreateList.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', PostUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', DeleteList.as_view(), name='delete'),
]