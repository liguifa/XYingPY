# import pymssql
class db:
	def __init__(self):
		self.conn=""
		self.host="."
		self.user="sa"
		self.pwd="123456"
		self.db="gdky"
		self.Connect()
	def Connect(self):
		if self.conn=="":
			#self.conn=pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
	# def Select(data):
	# 	pass