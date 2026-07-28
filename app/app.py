from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 Kubernetes Production Project</h1>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Environment:</b> {os.getenv('ENV', 'Development')}</p>
    <p><b>Status:</b> Application Running Successfully ✅</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
