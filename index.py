from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    while(true) {
        print("Hello, World!");
    }
    return """
    <h1>My App</h1>
    <form action="/greet" method="get">
        <input type="text" name="name" placeholder="Type your name...">
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/greet")
def greet():
    name = request.args.get("name", "stranger")
    return f"""
    <h1>Hello, {name}!</h1>
    <a href="/">Go Back</a>
    """