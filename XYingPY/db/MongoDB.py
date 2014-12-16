import pymongo
class db:
    def __init__(self):
        self.host="127.0.0.1"
        self.port="27017"
        self.database="foobar"
        self.conn=None
        self.db=None
        self.Connect()
    def Connect(self):
        if(self.conn==None):
            pdo=pymongo.Connection(self.host,self.port)
            self.db=self.conn[self.database]
    def Select():
        return self.db.persons.find()