from django.http import HttpResponse
from django.shortcuts import render
from design.menuregistry import menu_registry as register_menu
from design.submenuregistry import submenu_registry as register_submenu

@register_submenu('zfs', 'Filesystems', '/zfs/filesystem')
def filesystem(request):
    return render(request, 'zfs/filesystem.html')
