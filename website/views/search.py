from flask import Blueprint, render_template
from website.models.tables import Doctor


search = Blueprint('search', __name__)

@search.route('/')
def search_results():
    return render_template("pages/search.html")