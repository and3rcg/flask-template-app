from flask import Blueprint, render_template


frontend = Blueprint("frontend", __name__, url_prefix="/", template_folder="templates")

@frontend.route("/")
def homepage():
    return render_template("index.html")
