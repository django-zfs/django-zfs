from django import template
register = template.Library()

panel_types = {
				"ONLINE" : "panel-success",
				"FAILED" : "panel-danger",
				"DEGRADED" : "panel-warning"
				}

@register.filter(name="status_filter")
def status_filter(value):
	return panel_types.get(value, "panel-info")