import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

FLAG_PATH = Path("/flag")
HOST = os.environ.get("FLAG_SERVICE_HOST", "127.0.0.1")
PORT = int(os.environ.get("FLAG_SERVICE_PORT", "7601"))


class FlagHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/flag":
            self.send_error(404)
            return

        try:
            data = FLAG_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            self.send_error(404, "Flag missing")
            return
        except OSError:
            self.send_error(500, "Unable to read flag")
            return

        payload = data.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):  # noqa: A003
        # Silence default logging to avoid noisy stdout
        pass


def main():
    server = ThreadingHTTPServer((HOST, PORT), FlagHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
