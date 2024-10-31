import http.server
import socketserver
import time
from urllib.parse import urlparse, parse_qs

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Parse the URL and query parameters
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        print("flag is: %s" % query_params)

    def log_message(self, format, *args):
        # Override to print to console instead of error log
        print(f"{self.client_address[0]} - [{time.asctime()}] {format%args}")

def run_server(port=7777):
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"Server running on port {port}")
        print("Ready to receive messages. Send a GET request'")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
