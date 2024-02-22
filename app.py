from flask import Flask, render_template
# from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


# @app.route("/<name>")
# def hello_name(name):
#     return f"Hello, {escape(name)}!"


@app.route("/users")
def hello_users():
    return render_template("users.html")


@app.route("/users/<int:user_id>")
def hello_user(user_id):
    return f"Hello, user {user_id}!"


if __name__ == "__main__":
    app.run()
