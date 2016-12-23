from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from post import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.PostList.as_view(), name='home'),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
