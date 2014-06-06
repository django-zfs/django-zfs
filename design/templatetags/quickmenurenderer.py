from django import template
from django.shortcuts import render as template_render
from design.quickmenuregistry import quickmenu_registry

register = template.Library()

@register.tag(name="render_quickmenu")
def render_quickmenu(parser, token):
	return QuickMenuNode(token)

class QuickMenuNode(template.Node):
	def get_request(self,context):
		try:
			return template.Variable('request').resolve(context)
		except template.VariableDoesNotExist:
			return None
			
	def __init__(self, format_string):
		self.format_string = format_string
		self.registry = quickmenu_registry.list()
		
	def render(self, context):
		tpl = template.loader.select_template(['quickmenu.html'])
		return tpl.render(template.Context({'menu_items': self.registry}))
