from django.conf.urls import url

from zfs.views.overview import overview

urlpatterns = [
    url(r'^$', overview, name='overview')
]
