from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
from config.config import *


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            file_data = field_item.file.read()
            file_len = len(file_data)
            print(f'{field} is {file_len} bytes in length')

            # Save the file
            with open(field, 'wb') as f:
                f.write(file_data)

        # Respond with a 200 status
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=MyServer, port=PORT):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on device: {HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()