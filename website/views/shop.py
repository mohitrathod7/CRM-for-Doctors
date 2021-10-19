from flask import Blueprint, render_template


shop = Blueprint('shop', __name__)

@shop.route("/")
def home():
    return render_template("pages/shop/shop.html")
