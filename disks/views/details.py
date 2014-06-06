from django.http import HttpResponse
from django.shortcuts import render

from disks.tools.disks import get_block_device_details

def details(request, diskname=None):
	if diskname is None:
		raise Exception("Disk Parameter is required!")
	else:
		return render(request, 'disks/details.html',{'disk' : get_block_device_details(diskname)})