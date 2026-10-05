import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        self.wfile.write(
            b"CI/CD Hub - All Pass Demo"
        )


port = int(os.environ.get("PORT", "5000"))

HTTPServer(
    ("0.0.0.0", port),
    Handler
).serve_forever()
