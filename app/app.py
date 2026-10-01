from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        version = os.getenv("APP_VERSION", "unknown")
        body = f"Hello from Kubernetes - version {version}\n".encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
