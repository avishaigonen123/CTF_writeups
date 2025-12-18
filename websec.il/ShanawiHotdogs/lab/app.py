from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Pin Cracking Lab is Running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
