from flask import Blueprint, render_template, request
from auth import Auth

web = Blueprint("web", __name__)
auth_1 = Auth(request)

@web.route("/")
@auth_1.authorize
def t_home():
    return render_template("base.html")

@web.route("/login", methods=["GET", "POST"])
@auth_1.authenticate
def t_login():
    return render_template("login.html")