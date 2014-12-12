import types
class Views:
	def View(self,path,data):
		f=open(path)
		text=f.read()
		f.close()
		text=self.Rendering(text,data)
		return text
	def Rendering(self,text,data):
		for (d,v) in data.items():
			if type(v) is types.ListType:
				str_start="@foreach_"+d
				str_end="@forend_"+d
				arr_header=text.split(str_start)
				arr_footer=arr_header[1].split(str_end)
				str_temp=""
				for kk, vv in enumerate(v):
					str_temp=arr_footer[0]
					for (d_str,v_str) in vv.items():
						str_temp=str_temp.replace('@'+d_str,v_str)
					arr_header[0]+=str_temp
				text=arr_header[0]+arr_footer[1]
			else:
				text=text.replace('@'+d,v)
		return text