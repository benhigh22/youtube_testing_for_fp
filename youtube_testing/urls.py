from django.conf.urls import url
from django.contrib import admin

from app.views import IndexView, VideoView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<url>.+)', VideoView.as_view(), name='video_view')
]
