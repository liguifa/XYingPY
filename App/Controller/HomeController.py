from XYingPY.lib.Controller import Controller
from XYingPY.lib.Model import Model
class Test:
    def __init__(self):
        self.name="Test"
        self.img="nan"
        self.age="21"
class HomeController(Controller):
    def index(self):
        t=Test()
        self.DataContext("user",t)
        dict_arr = [{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title 2', 'body':'this is body 2','url':'App/Themes/Image/jeki_chan.jpg'}]
        self.DataContext("tech",dict_arr)
        self.View()
    def LoadTech(self):
        dict_arr = [{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title', 'body':'this is body','url':'App/Themes/Image/jeki_chan.jpg'},{'title': 'this is title 2', 'body':'this is body 2','url':'App/Themes/Image/jeki_chan.jpg'}]
        self.Json(dict_arr)
    def content(self):
        self.View()
    def login(self):
        self.View()
    def loginIn(self):
        dict_arr = [{'title': 'this is title', 'body':'this is body'},{'title': 'this is title 2', 'body':'this is body 2'}]
        self.Json(dict_arr)
    def test(self):
        self.VerCode()