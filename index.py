from flask import Flask

# ✅ Vercel looks for this variable named "app"
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Vercel!"

# ⚠️ Keep this ONLY for local testing
if __name__ == "__main__":
    app.run(debug=True)