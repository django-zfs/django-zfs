from django.http import HttpResponse
from django.shortcuts import render
from design.menuregistry import menu_registry as register_menu
from design.submenuregistry import submenu_registry as register_submenu

from zfs.tools.zpool import get_all_zpools

@register_menu('ZFS', '/zfs')
@register_submenu('zfs', 'Overview', '/zfs')
def overview(request):
    return render(request, 'zfs/overview.html', {'pools' : get_all_zpools()})
