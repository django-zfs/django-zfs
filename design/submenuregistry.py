from collections import defaultdict

class SubMenuRegistry():
	registry = defaultdict(list)
	def __call__(self, app, name, url):
		def __inner(func):
			self.registry[app].append({'name' : name, 'url' : url})
			return func
		return __inner
	def list(self, appname):
		return self.registry[appname]
		
submenu_registry = SubMenuRegistry()

