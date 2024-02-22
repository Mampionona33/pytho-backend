from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"


@app.route("/user/<int:user_id>")
def hello_user(user_id):
    return f"Hello, user {user_id}!"


if __name__ == "__main__":
    app.run()
