from ..lib.request import request
from App.Controller.HomeController import HomeController
import types
class route:
    @staticmethod
    def start():
        C=request.getParameters("c")
        A=request.getParameters("a")
        c=globals()["HomeController"]() if type(C) is types.NoneType else globals()[C+"Controller"]()
        a=getattr(c,"index") if type(A) is types.NoneType else getattr(c,A)
        a()
