class QuickMenuRegistry():
	registry = {}
	def __call__(self, name, url):
		def __inner(func):
			self.registry[name] = url
			return func
		return __inner
	def list(self):
		return self.registry
		
quickmenu_registry = QuickMenuRegistry()

