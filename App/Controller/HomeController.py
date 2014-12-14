from XYingPY.lib.Controller import Controller
# from XYingPY.lib.Model import Model
class HomeController(Controller):
    def index(self):
        self.DataContext("name","234")
        dict_arr = [{'title': 'this is title', 'body':'this is body'},{'title': 'this is title 2', 'body':'this is body 2'}]
        self.DataContext("news",dict_arr)
        self.View()
    def content(self):
        self.View()
    def login(self):
        self.View()
    def loginIn(self):
        dict_arr = [{'title': 'this is title', 'body':'this is body'},{'title': 'this is title 2', 'body':'this is body 2'}]
        self.Json(dict_arr)
    def test(self):
        self.VerCode()
