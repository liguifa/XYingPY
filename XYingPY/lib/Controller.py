from request import request
from Views import Views
class Controller:
	def __init__(self):
		self.data={}
	def View(self):
		path="App/Views/"+request.getParameters("c")+"/"+request.getParameters("a")+".html"
		v=Views()
		text=v.View(path,self.data)
		print "Content-type: text/html"
		print ""
		print text
	def Show(self,string):
		print "Content-type: text/text"
		print ""
		print string
	def DataContext(self,name,value):
		self.data[name]=value