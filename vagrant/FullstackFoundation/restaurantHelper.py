

def turnHtml(name, idnr):
	return ("<p>"+name+'''<br>
		<a href='http://localhost:8080/restaurants/%s/edit'>Edit</a><br>
		<a href='http://localhost:8080/restaurants/%s/delete'>Delete</a><br></p>\n''' % (idnr, idnr) )


	#<a href='http://localhost:8080/restaurants/delete"