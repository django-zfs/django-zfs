import json
import re
from libzfs.zpool import *
from libzfs.handle import LibZFSHandle
from libzfs.bindings.generic.libzfs.enums import zpool_prop

def get_all_zpools():
	pools = list()
	for pool in ZPool.list():
		with LibZFSHandle():
			properties = dict(pool.properties.items())
			pools.append(
				{
					'name': pool.name,
					'status': pool.status,
					'state': pool.state,
					'size': properties.get(zpool_prop.SIZE, 0),
					'capacity': re.sub('%', '', properties.get(zpool_prop.CAPACITY, '0')),
					'dedupratio': properties.get(zpool_prop.DEDUPRATIO, 0),
					'free': properties.get(zpool_prop.FREE, 0),
					'allocated': properties.get(zpool_prop.ALLOCATED, 0),
					'config' : pool.config.get('vdev_tree',None),
					'type' : pool.config.get('type', None)
				})
	return pools