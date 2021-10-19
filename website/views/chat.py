from flask import Blueprint, render_template

chat = Blueprint('chat', __name__)

@chat.route("/")
def home():
    return render_template("pages/chat/chat.html")
