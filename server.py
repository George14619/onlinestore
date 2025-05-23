from flask import Flask, request
import json
from config import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # warning: this disables CORS policy


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

################################################################################
##########################       API         ###################################
################################################################################

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
    return "Hello " + name
    # return f"Hello {name}"


@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user_name = "Pam"
    age = 25
    return "contact"



products = []
@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)
        


    return json.dumps(categories)


@app.get("/api/reports/total")
def get_total():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)   

# post
@app.post("/api/products")
def post_products():
    item = request.get_json()
    print(item)
    
    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))


# put
@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item = request.get_json()
    if len(products) > index >= 0:
        products[index]= updated_item
        return json.dumps(updated_item)
    else:
        return "that index does not exist"


# Try to use the delete method
# delete
@app.delete("/api/products/<int:index>")
def delete_product(index):
    deleted_item = request.get_json()
    if 0<= index < len(products):
        deleted_item = products.pop(index)
        return json.dumps(deleted_item)
    else:
        return "That index does not exist"


# patch
@app.patch("/api/products/<int:index>")
def patch_product(index):
    patch_item = request.get_json()
    if 0<= index < len(products):
        products(index).index(patch_item)
        return json.dumps(patch_item)
    else:
        return "That index does not exist"
    


# @app.post
# @app.put
# @app.delete
# @app.patch

#####################################
########### API COUPONS #############
#####################################


@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()

    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    results = []
    cursor = db.coupons.find({})
    for cp in cursor:
        results.append(fix_id(cp))

    return json.dumps(results)    


app.run(debug=True, port=8000)