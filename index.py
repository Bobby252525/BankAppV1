from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return greet()

def greet():
    return """
    <h1 style="text-align: center;">Hi, please fill out the form below:</h1>
    <form action="/submitted" method="get">
        <p>Enter your full legal name</p>
        <p><input type="text" name="name" placeholder="Enter" required></p>
        <p>Please enter your birthdate</p>
        <p><input type="date" name="birthdate" required></p>
        <p>Enter any previous work experience</p>
        <p><input type="text" name="Job" placeholder="Enter" required></p>
        <p>Enter years of work experience</p>
        <p><input type="number" name="Exp" placeholder="Enter" required></p>
        <button type="submit">Submit</button>
    </form>
    """
    # name = "Alice"
    # age = int(input("Enter your age: "))

    # # Build the output as a string
    # result = ""

    # result += "Hello, " + name + "!\n"
    # result += "You are " + str(age) + " years old.\n\n"

    # # Simple math
    # a = 10
    # b = 5
    # result += "Sum: " + str(a + b) + "\n"
    # result += "Difference: " + str(a - b) + "\n"
    # result += "Product: " + str(a * b) + "\n"
    # result += "Division: " + str(a / b) + "\n\n"

    # # If statement
    # if age >= 18:
    #     result += name + " is an adult.\n"
    # else:
    #     result += name + " is a minor.\n"

    # # Loop
    # result += "Counting to 5:\n"
    # for i in range(1, 6):
    #     result += str(i) + "\n"

    # return result  # ✅ return instead of print

# if __name__ == "__main__":
#     print(greet())
@app.route("/submitted")
def submitted():
    return "Thank you for submitting the form!"