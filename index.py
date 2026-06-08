from flask import Flask

app = Flask(__name__)

# --- Home Page ---
@app.route("/")
def home():
    return "Hello World!"

# ✅ ADD YOUR NEW ROUTES BELOW HERE

@app.route("/about")
def about():
    return "This is the about page!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"