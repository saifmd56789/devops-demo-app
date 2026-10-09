from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Welcome to DevOps Demo App</h1>
    <p>Version: 1.0</p>
    <p>Environment: Production</p>
    <p>Status: Healthy</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)