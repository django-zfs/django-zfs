from django.conf.urls import url

from zfs.views.overview import overview
from zfs.views.filesystem import filesystem
from zfs.views.pool import pool

urlpatterns = [
	url(r'filesystem/^$', filesystem, name='filesystem'),
	url(r'pool/^$', pool, name='pool'),
    url(r'^$', overview, name='overview')
]
