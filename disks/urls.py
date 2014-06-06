from django.conf.urls import url

from disks.views.overview import overview
from disks.views.details import details

urlpatterns = [
	url(r'^details/(?P<diskname>.*)', details, name='details'),
    url(r'^$', overview, name='overview')
]
