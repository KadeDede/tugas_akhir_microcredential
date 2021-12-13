from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World! Deploy nich...</p>"
#
# @app.route("/works")
# def it_works():
#     return "IT Works! nyehehe"
from app import routes


if __name__ == '__main__':
    app.debug = True
    app.run()