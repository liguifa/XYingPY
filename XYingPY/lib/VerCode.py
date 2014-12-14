import random
from PIL import Image
class VerCode:
    def __init__(self):
        self.code=""
    def ProduceNum(self):
        i=1
        while (i<=4):
            i=i+1
            self.code+=str(int(random.uniform(0,9)))
    def CreateVerCode(self):
        im=Image.open("__verCode.png")
        print "123"
        print im.format, im.size, im.mode
    def GetCode(self):
        self.CreateVerCode()
        return self.code
v=VerCode()
v.GetCode()