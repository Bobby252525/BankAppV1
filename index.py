from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style="text-align: center;">Please Fill Out This Form:</h1>
    <form action="/Personal" method="get">
        <p>Full legal name</p>
        <input type="text" name="name" placeholder="Enter" required>
        <p>Birthdate</p>
        <input type="date" name="birthdate" required>
        <p>Previous work experience</p>
        <input type="text" name="Job" placeholder="Enter" required>
        <p>Years of experience</p>
        <input type="number" name="Exp" placeholder="Enter" required>
        <p><button type="submit">Next</button></p>
    </form>
    """

@app.route("/Personal")
def Personal():
    name = request.args.get("name", "null")
    birthdate = request.args.get("birthdate", "null")
    job = request.args.get("Job", "null")
    exp = request.args.get("Exp", "null")

    return f"""
    <h1 style="text-align: center;">Please Fill Out This Form:</h1>
    <form action="/submit" method="get">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="birthdate" value="{birthdate}">
        <input type="hidden" name="Job" value="{job}">
        <input type="hidden" name="Exp" value="{exp}">
        <p>SSN</p>
        <input type="number" name="SSN" placeholder="Enter" required>
        <p>Address</p>
        <input type="text" name="Address" placeholder="Enter" required>
        <p>Phone number</p>
        <input type="number" name="Phone" placeholder="Enter" required>
        <p><button type="submit">Submit</button></p>
    </form>
    """
@app.route("/submit")
def Submit():
    name = request.args.get("name", "null")
    birthdate = request.args.get("birthdate", "null")
    job = request.args.get("Job", "null")
    exp = request.args.get("Exp", "null")
    ssn = request.args.get("SSN", "null")
    address = request.args.get("Address", "null")
    phone = request.args.get("Phone", "null")

    return f"""
    <form action="/info" method="get">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="birthdate" value="{birthdate}">
        <input type="hidden" name="Job" value="{job}">
        <input type="hidden" name="Exp" value="{exp}">
        <input type="hidden" name="SSN" value="{ssn}">
        <input type="hidden" name="Address" value="{address}">
        <input type="hidden" name="Phone" value="{phone}">
        <h1 style="text-align: center;">Thank You For the Submission!</h1>
        <p><button type="submit">View Stolen Information</button></p>
    """




@app.route("/info")
def Info():
    name = request.args.get("name", "null")
    birthdate = request.args.get("birthdate", "null")
    job = request.args.get("Job", "null")
    exp = request.args.get("Exp", "null")
    ssn = request.args.get("SSN", "null")
    address = request.args.get("Address", "null")
    phone = request.args.get("Phone", "null")

    return f"""
    <h1 style="text-align: center;">Our Information</h1>
    <p>Name: {name}</p>
    <p>Birthdate: {birthdate}</p>
    <p>Job: {job}</p>
    <p>Experience: {exp} years</p>
    <p>SSN: {ssn}</p>
    <p>Address: {address}</p>
    <p>Phone: {phone}</p>
    """