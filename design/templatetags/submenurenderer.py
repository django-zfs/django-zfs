from django import template
from django.shortcuts import render as template_render
from design.submenuregistry import submenu_registry

from django.apps import AppConfig

register = template.Library()

@register.tag(name="render_submenu")
def render_submenu(parser, token):
	return SubMenuNode(token)

class SubMenuNode(template.Node):			
	def __init__(self, token):
		tag_name, app_name = token.split_contents()
		self.app = app_name
		self.menu = submenu_registry.list(self.app)
		
	def render(self, context):
		tpl = template.loader.get_template('submenu.html')
		
		submenu = self.menu
		if not submenu:
			raise Exception("Cannot render submenu without any items")
		return tpl.render(template.Context({'menu_items': submenu}))
