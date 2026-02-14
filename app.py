from flask import Flask, render_template, request, redirect, url_for
from app.services.material_service import get_materials
from app.services.purchase_service import save_purchase
from app.services.inventory_service import save_inventory


app = Flask(__name__)
app.secret_key = "dev-secret-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        purchase_date = request.form["purchase_date"]
        material_id = request.form["material_id"]
        quantity = request.form["quantity"]
        amount = request.form["amount"]

        save_purchase(purchase_date, material_id, quantity, amount)

        return redirect(url_for("purchase"))

    materials = get_materials()
    return render_template("purchase.html", materials=materials)

@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        inventory_date = request.form["inventory_date"]
        material_id = request.form["material_id"]
        actual_quantity = request.form["actual_quantity"]

        save_inventory(
            inventory_date,
            material_id,
            actual_quantity
        )

        return redirect(url_for("inventory"))

    materials = get_materials()
    return render_template("inventory.html", materials=materials)


if __name__ == "__main__":
    app.run(debug=True)
