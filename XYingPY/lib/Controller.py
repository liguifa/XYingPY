from request import request
from Views import Views
from VerCode import VerCode
import types
class Controller:
    def __init__(self):
        self.data={}
    def View(self):
        C=request.getParameters("c")
        A=request.getParameters("a")
        c="Home" if type(C) is types.NoneType else C
        a="index" if type(A) is types.NoneType else A
        path="App/Views/"+c+"/"+a+".html"
        v=Views()
        text=v.View(path,self.data)
        print "Content-type: text/html"
        print ""
        print text
    def Show(self,string):
        print "Content-type: text/html"
        print ""
        print string
    def Json(self,arr):
        if type(arr) is types.ListType:
            num=0
            string="["
            for kk, vv in enumerate(arr):
                num=num+1
                string+="{"
                for (d,v) in vv.items():
                    string+="\""+d+"\":\""+v+"\","
                string=string[0:-1]+"},"
            string="{\"total\":"+str(num)+",\"rows\":"+string[0:-1]+"]}"
        else:
            string=""
        print "Content-type: text/html"
        print ""
        print string
    def DataContext(self,name,value):
        self.data[name]=value
    def VerCode(self):
        print "Content-type: text/html"
        print ""
        v=VerCode()
        print v.GetCode()