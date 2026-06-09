from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return Basic()

def Basic():
    return f"""
    <h1 style="text-align: center;">Hi, please fill out the form below:</h1>
    <form action="/info" method="get">
        <p>Enter your full legal name</p>
        <p><input type="text" id="name" placeholder="Enter" required></p>
        <p>Please enter your birthdate</p>
        <p><input type="date" name="birthdate" required></p>
        <p>Enter any previous work experience</p>
        <p><input type="text" name="Job" placeholder="Enter" required></p>
        <p>Enter years of work experience</p>
        <p><input type="number" name="Exp" placeholder="Enter" required></p>
    </form>
    <form action="/Personal" method="get">
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
@app.route("/Personal")
def Personal():
    name = __name__
    return f"""
    <form action="/info" method="get">
        <h1 style="text-align: center;">Please fill out the form below:</h1>
        <p>Enter your SSN</p>
        <p><input type="number" name="SSN" placeholder="Enter" required></p>
        <p>Enter your address</p>
        <p><input type="text" name="Address" placeholder="Enter" required></p>
        <p>Enter your phone number</p>
        <p><input type="number" name="Phone" placeholder="Enter" required></p>
    </form>
    <form action="/submitted" method="get">
        <button type="submit">Submit</button>
    </form>


    """

@app.route("/submitted")
def submitted():
    return f"""
    <form action="/info" method="get">
        <p>Thank you for submitting your information</p>
        <button type="submit">View stolen information</button>
    </form>


    """

@app.route("/info")
def Info():
    name = request.args.get("name", "null")
    birthdate = request.args.get("birthdate", "null")
    Job = request.args.get("Job", "null")
    Exp = request.args.get("Exp", "null")
    SSN = request.args.get("SSN", "null")
    Address = request.args.get("Address", "null")
    Phone = request.args.get("Phone", "null")
    return f"""
    <h1 style="text-align: center;">Personal Information</h1>
    <h1>Name: {name}</h1>
    <h1>Birthdate: {birthdate}</h1>
    <h1>Previous Work Experience: {Job}</h1>
    <h1>Years of Work Experience: {Exp}</h1>
    <h1>SSN: {SSN}</h1>
    <h1>Address: {Address}</h1>
    <h1>Phone Number: {Phone}</h1>
    
    
    
    """