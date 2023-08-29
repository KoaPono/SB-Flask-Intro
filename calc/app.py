from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def subtraction():
    """Subtract a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mulitplication():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def division():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

@app.route("/math/<operation>")
def math(operation):
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    if operation == "add":
        result = add(a, b)
    elif operation == "sub":
        result = sub(a, b)
    elif operation == "mult":
        result = mult(a, b)
    elif operation == "div":
        result = div(a, b)

    return str(result)