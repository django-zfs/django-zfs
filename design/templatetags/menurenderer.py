from django import template
from django.shortcuts import render as template_render
from design.menuregistry import menu_registry

register = template.Library()

@register.tag(name="render_menu")
def render_menu(parser, token):
	return MenuNode(token)

class MenuNode(template.Node):			
	def __init__(self, format_string):
		self.format_string = format_string
		self.registry = menu_registry.list()
		
	def render(self, context):
		tpl = template.loader.select_template(['menu.html'])
		return tpl.render(template.Context({'menu_items': self.registry}))
