import random
class VerCode:
	def __init__(self):
		self.code=""
	def ProduceNum(self):
		i=1
		while (i<=4):
			i=i+1
			self.code+=str(int(random.uniform(0,9)))
	def CreateVerCode(self):
		import Image
		print "123"
		im=Image.open("C:/Users/liguifa/Desktop/__verCode.png")
		print im.format, im.size, im.mode
	def GetCode(self):
		self.CreateVerCode()
		return self.code