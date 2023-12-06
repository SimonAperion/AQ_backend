import http.server
import socketserver
import os

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the default path to 'index.html'
        self.path = '/index.html'
        try:
            # Try to serve the requested file
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        except FileNotFoundError:
            # If the file is not found, serve 'index.html'
            self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set the current working directory to the build directory of your React app
# Replace 'path/to/your/react/app/build' with the actual path
os.chdir('./build')

# Use a higher port number if 8080 is already in use
port = 8080

# Start the server with the custom request handler
with socketserver.TCPServer(("", port), CustomRequestHandler) as httpd:
    print(f"Serving at http://localhost:{port}")
    print("Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
