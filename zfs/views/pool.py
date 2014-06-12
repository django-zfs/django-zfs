from django.http import HttpResponse
from django.shortcuts import render
from design.menuregistry import menu_registry as register_menu
from design.submenuregistry import submenu_registry as register_submenu

@register_menu('ZFS', '/zfs')
@register_submenu('zfs', 'Pools', '/zfs/pools')
def pool(request):
    return render(request, 'zfs/pools.html')
