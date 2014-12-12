from ..lib.request import request
from App.Controller.HomeController import HomeController
class route:
	@staticmethod
	def start():
		C=request.getParameters("c")
		A=request.getParameters("a")
		c=globals()[C+"Controller"]()
		a=getattr(c,A)
		a()