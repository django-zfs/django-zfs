from django.http import HttpResponse
from django.shortcuts import render
from design.menuregistry import MenuRegistry
from design.submenuregistry import SubMenuRegistry

from disks.tools.disks import get_block_devices

menuregister = MenuRegistry()
submenuregister = SubMenuRegistry()

@menuregister('Disks', '/disks')
@submenuregister('disks', 'Overview', '/disks')
def overview(request):
	return render(request, 'disks/overview.html',{'disktable' : get_block_devices()})