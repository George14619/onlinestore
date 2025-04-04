from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World CH56!</p>"


@app.get("/test")
def test():
    return "This is a test endpoint 1.0."


@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the home page!"


@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}


@app.get("/api/about")
def about():
    print("About endpoint accessed")
    name = {"name": "Leo Miranda"}
    return name


@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Jeffrey", "George", "Nar", "Rafael", "Isai", "Erick"]
    return student_names


@app.get("/greet/<name>")
def greet(name):
    print("Greet endpoint accessed")
    # return "Hello " + name
    return f"Hello {name}"


@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user_name = "Pam"
    age = 25
    return render_template("contact.html", name=user_name, age=age)


# @app.post
# @app.put
# @app.delete
# @app.patch

app.run(debug=True, port=8000)