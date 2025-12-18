import base64
import getpass
import os
from base64 import b64decode

import requests
from flask import Flask, Response, abort, render_template, request
from werkzeug.debug import DebuggedApplication, get_pin_and_cookie_name

DebuggedApplication._fail_pin_auth = lambda self: print("No bruteforce allowed.", flush=True)

app = Flask(__name__)
app.debug = True
FLAG_ENDPOINT = os.environ.get("FLAG_SERVICE_URL", "http://127.0.0.1:7601/flag")


# @app.route('/img/<path>')
# def get_image(path: str):
#     path = b64decode(path).decode()
#     image_path = os.path.join('static/', path)
#     try:
#         with open(image_path, 'rb') as file:
#             payload = base64.b64encode(file.read()).decode()
#             return Response(payload, mimetype='text/plain')
#     except Exception as e:
#         return str(e), 500

# @app.route("/whoami")
# def whoami(): # TODO: remove this function, used to debug the container
#     return f'{getpass.getuser()}'

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/flag')
# def flag():
#     pin, _ = get_pin_and_cookie_name(app)
#     secret_pin = request.cookies.get('secret_pin', '')
#     if not (secret_pin and secret_pin == pin):
#         return 'You didn\'t enter the right pin!', 403

#     try:
#         response = requests.get(FLAG_ENDPOINT, timeout=2)
#     except requests.RequestException:
#         return "Flag service offline", 503

#     if response.status_code != 200:
#         return "Flag service error", response.status_code
#     return response.text, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    
