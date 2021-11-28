from flask import Flask,session,redirect,render_template,request
import tokens

website = Flask(__name__)
website.secret_key = "12345"

@website.route("/")
def index():
    if "token" in session:
        token = session["token"]
        verify = tokens.check(token)
        if verify:
            return render_template("index.html",username=verify,token=token)
        else:
            session.pop("token")
    return redirect("/login")

@website.route("/logout")
def logout():
    if "token" in session:
        session.pop("token")
    return redirect("/login")

@website.route("/login")
def login():
    return render_template("login.html")
@website.route("/register")
def register():
    return render_template("register.html")

@website.route("/login",methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    verify = tokens.check_login(username,password)
    if verify:
        session["token"] = tokens.get()[username]["token"]
        return redirect("/")
    else:
        return "no"

@website.route("/register",methods=["POST"])
def register_post():
    username = request.form["username"]
    password = request.form["password"]

    tokens.add(username,password)
    session["token"] = tokens.get()[username]["token"]
    return redirect("/")

@website.route("/change")
def change_token():
    if "token" in session:
        token = session["token"]
        verify = tokens.check(token)
        if verify:
            tokens.update_user(verify)
            session.pop("token")
    return redirect("/login")
website.run("0.0.0.0",80)