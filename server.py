from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/cupcakes-individual/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    
    if cupcake:
        return render_template("individual-cupcake.html", cupcake = cupcake)
    else:
        return "404 not found"

@app.route("/order")
def order():
    return render_template("order.html", order = get_cupcakes("orders.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    
    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("order"))
    else:
        return "Sorry cupcake not found."
    

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")