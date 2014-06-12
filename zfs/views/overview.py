from django.http import HttpResponse
from django.shortcuts import render
from design.menuregistry import menu_registry as register_menu
from design.submenuregistry import submenu_registry as register_submenu

from zfs.tools import zfs as zfs_tools

@register_menu('ZFS', '/zfs')
@register_submenu('zfs', 'Overview', '/zfs')
def overview(request):
    return render(request, 'zfs/overview.html', {'pools' : zfs_tools.get_all_pool_info()})
