# Simple Python Example
from flask import Flask

# ✅ Vercel looks for this variable named "app"
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Vercel!"

# ⚠️ Keep this ONLY for local testing
if __name__ == "__main__":
    app.run(debug=True)
# Variables
name = "Alice"
age = 25

# Print a greeting
print("Hello, " + name + "!")
print("You are", age, "years old.")

# Simple math
a = 10
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)

# If statement
if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is a minor.")

# Loop
print("Counting to 5:")
for i in range(1, 6):
    print(i)