from flask import Blueprint, render_template
from auth import Auth

web = Blueprint("api", __name__)

@web.route("/")
def r_home():
    return render_template("base.html")