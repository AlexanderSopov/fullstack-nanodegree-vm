from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from restaurantDB import getAllRestaurants, addRestaurant, editRestaurant, deleteRestaurant

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<a href='http://localhost:8080/restaurants/new'>Make a new Restaurant</a>"
				output += getAllRestaurants()
				output += "</body></html>"
				self.wfile.write(output)

				print output
				return

			if self.path.endswith("/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><h1>Make a New Restaurant"
				output += '''<form method='POST' enctype='multipart/form-data'
action='/restaurants/new'>
<input name="new restaurant" type="text" placeholder="Make new Restaurant" >
<input type="submit" value="Create"> </form>'''
				
				output += "</body></html>"
				self.wfile.write(output)
				print output
		



			if self.path.endswith("/edit"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><h1>Edit Restaurant"
				output += '''<form method='POST' enctype='multipart/form-data'
action='%s'>
<input name="editRestaurant" type="text" placeholder="Edit Restaurant" >
<input type="submit" value="Edit"> </form>''' %self.path
				
				output += "</body></html>"
				self.wfile.write(output)
				print output


			if self.path.endswith("/delete"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><h1>are you sure you want to delete restaurant?"
				output += '''<form method='POST' enctype='multipart/form-data'
action='%s'>
<input type="submit" value="Delete"> </form>''' %self.path
				
				output += "</body></html>"
				self.wfile.write(output)
				print output


		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


	def do_POST(self):
		try:
			if self.path.endswith("/new"):
				ctype, pdict = cgi.parse_header(
					self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('new restaurant')
				message = messagecontent[0]
				addRestaurant(message)


				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()


		
			if self.path.endswith("/edit"):
				ctype, pdict = cgi.parse_header(
				self.headers.getheader('content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('editRestaurant')
				message = messagecontent[0]

				idstr = self.path
				idstr = idstr[13:(len(idstr)-5)]
				idnr = int(idstr)

				editRestaurant(message, idnr)

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()


			if self.path.endswith("/delete"):
				print "Got here first"
				ctype, pdict = cgi.parse_header(
				self.headers.getheader('content-type'))

				idstr = self.path
				idstr = idstr.split("/")[2]
				idnr = int(idstr)
				print "Got here"
				deleteRestaurant(idnr)

				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()

		except:
			pass



def main():
	try:
		port = 8080
		server = HTTPServer(('',port), webserverHandler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()


if __name__ == '__main__':
	main()
