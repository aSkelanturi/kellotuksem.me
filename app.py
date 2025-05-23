import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config
import chugs
import users

app = Flask(__name__)
app.secret_key = config.secret_key

#Check login
def require_login():
    if "user_id" not in session:
        abort(403)

#Front page
@app.route("/")
def index():
    all_chugs = chugs.get_chugs()
    return render_template("index.html", chugs=all_chugs)

#user info pages
@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    chugs = users.get_chugs(user_id)
    return render_template("show_user.html", user = user, chugs = chugs)

#searching fucntion
@app.route("/find_chug")
def find_chug():
    query = request.args.get("query")
    if query:
        results = chugs.find_chugs(query)
    else:
        query = ""
        results = []
    return render_template("find_chug.html", query=query, results=results)

#Chug info pages
@app.route("/chug/<int:chug_id>")
def show_chug(chug_id):
    chug = chugs.get_chug(chug_id)
    if not chug:
        abort(404)
    return render_template("show_chug.html", chug = chug)


#Chug adding form
@app.route("/new_chug")
def new_chug():
    require_login()
    return render_template("new_chug.html")

#Adding chugs
@app.route("/create_chug", methods=["POST"])
def create_chug():
    require_login()

    drink = request.form["drink"]
    if len(drink) > 50:
        abort(403)
    amount = request.form["amount"]
    if len(amount) > 5:
        abort(403)
    alcohollevel = request.form["alcohollevel"]
    if len(alcohollevel) > 5:
        abort(403)    
    carbonation = "carbonation" in request.form
    user_id = session["user_id"]

    

    #Getting the time as milliseconds
    minutes  = int(request.form.get("minutes",0))
    seconds  = int(request.form.get("seconds",0))
    milliseconds  = int(request.form.get("milliseconds",0))

    total_time = (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

    feeling = request.form["feeling"]
    
    chugs.add_chug(drink, total_time, amount, alcohollevel, carbonation, user_id, feeling)

    return redirect("/")

#chug editing page
@app.route("/edit_chug/<int:chug_id>")
def edit_chug(chug_id):
    require_login()
    chug = chugs.get_chug(chug_id)
    if not chug:
        abort(404)
    if chug["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_chug.html", chug = chug)

#update chug
@app.route("/update_chug", methods=["POST"])
def update_chug():
    require_login()
    chug_id = request.form["chug_id"]
    chug = chugs.get_chug(chug_id)
    if not chug:
        abort(404)
    if chug["user_id"] != session["user_id"]:
        abort(403)
    drink = request.form["drink"]
    if len(drink) > 50:
        abort(403)    
    amount = request.form["amount"]
    if len(drink) > 5:
        abort(403)
    alcohollevel = request.form["alcohollevel"]
    if len(drink) > 5:
        abort(403)    
    carbonation = "carbonation" in request.form
    user_id = session["user_id"]

        #Getting the time as milliseconds
    minutes  = int(request.form.get("minutes",0))
    seconds  = int(request.form.get("seconds",0))
    milliseconds  = int(request.form.get("milliseconds",0))

    total_time = (minutes * 60 * 1000) + (seconds * 1000) + milliseconds
    
    chugs.update_chug(chug_id, drink, total_time, amount, alcohollevel, carbonation)

    return redirect("/chug/" + str(chug_id))

#chug deleting page
@app.route("/remove_chug/<int:chug_id>", methods=["GET", "POST"])
def remove_chug(chug_id):
    require_login()
    chug = chugs.get_chug(chug_id)
    if not chug:
        abort(404)
    if chug["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_chug.html", chug = chug)
    if request.method == "POST":
        if "remove" in request.form:
            chugs.remove_chug(chug_id)
            return redirect("/")
        else:
            return redirect("/chug/" + str(chug_id))
        
# Registering page
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

#Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])
        
        if not result:
            return "VIRHE: väärä tunnus tai salasana"
        
        user_id = result[0]["id"]
        password_hash = result[0]["password_hash"]
        
        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"
#Logut page
@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["username"]
        del session["user_id"]
    return redirect("/")
