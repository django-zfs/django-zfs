import subprocess
from reparted import *
from celery import shared_task

dev_pattern = ['sd.*', 'mmcblk*', 'vd.*']

def get_block_devices():
	devices = []
	raw = subprocess.check_output(['lsblk','-lnbd']).split('\n')

	for line in raw:
			splitted = line.split()
			if len(splitted) < 1:
				continue

			disk = {
					'name' : splitted[0],
					'removable' : True if splitted[2] is '1' else False,
					'size' : splitted[3],
					'readonly' : True if splitted[4] is '1' else False,
					'type' : splitted[5],
				}
			devices.append(disk)
	return devices

def get_block_device_details(diskname):
	disk = Disk(Device("/dev/" + str(diskname)))
	result = {
		'name' : disk.device.path,
		'type' : disk.type_name,
		'size' : disk.size,
		'free' : disk.usable_free_space,
		'partitions' : disk.partitions()
	}
	return result