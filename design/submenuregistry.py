class SubMenuRegistry():
	registry = {}
	def __call__(self, app, name, url):
		def __inner(func):
			self.registry[app] = {name : url}
			return func
		return __inner
	def list(self):
		return self.registry
		
submenu_registry = SubMenuRegistry()

