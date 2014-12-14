# import pymssql
class db:
    def __init__(self):
        self.conn=""
        self.host="."
        self.user="sa"
        self.pwd="123456"
        self.db="gdky"
        self.Connect()