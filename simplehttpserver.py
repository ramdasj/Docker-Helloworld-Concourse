
import os
import BaseHTTPServer

class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def response_info(self, message):
		self.wfile.write('<html><body>')
		self.wfile.write(message)
		self.wfile.write('</body></html>')

	def do_GET(self):
		'''
		Handle a GET request.
		'''
		print self.path

		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		
		idx = self.path.find('?')
		query = ""
		if idx >= 0:
			endpoint = self.path[:idx]
			query = self.path[idx+1:]
		else:
			endpoint = self.path

		message = ""
		if endpoint == "/hello":
			message = "hello"
		elif endpoint == "/world":
			message = "world"
		elif endpoint == "/":
			message = "hello world"
		
		if query == "uppercase":
			message = message.upper()
		elif query == "reversed":
			message = message[::-1]
		
		self.response_info(message)

server = BaseHTTPServer.HTTPServer(("", 8080), MyRequestHandler)
try:
	server.serve_forever()
except KeyboardInterrupt:
	pass
server.server_close()
