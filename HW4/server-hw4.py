from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract the file path
        file_path = self.path.lstrip("/")  # Remove leading slash to get the file name
        mime_type, _ = mimetypes.guess_type(file_path)

        if mime_type == "text/html":
            try:
                # Open and read the HTML file
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Send a 200 response
                self.send_response(200)
                self.send_header("Content-Type", mime_type)
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                # Send a 404 File Not Found error
                self.send_error(404, f"File Not Found: {file_path}")

        elif mime_type == "application/json":
            try:
                # Open and read the JSON file
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Send a 200 response
                self.send_response(200)
                self.send_header("Content-Type", mime_type)
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                # Send a 404 File Not Found error
                self.send_error(404, f"File Not Found: {file_path}")

        else:
            # Handle unsupported content type
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found - Unsupported Content Type")

# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()