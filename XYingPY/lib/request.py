import cgi, cgitb 
class request:
	@classmethod
	def getParameters(self,name):
		form = cgi.FieldStorage()
		return form.getvalue(name)	