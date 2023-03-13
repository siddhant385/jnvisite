
from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from additionalsfunctions import matchpass




# configurable parameters
def param():
    """To read configurable items"""
    with open("templates/config.json") as f:
        a  = json.load(f)
        f.close()
        return a["params"]
# create the extension

db = SQLAlchemy()
# create the app
app = Flask(param()["app"])
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# initialize the app with the extension
db.init_app(app)

class UserData(db.Model):
    email = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    mobileno = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def hellowworld():
    return render_template("hellow.html" ,Blogging=param()["site_name"])

@app.route("/user")
def user(id):
    pass
    
def printUserandpass():
    user = db.session.execute(db.select(UserData.email,UserData.password)).scalars()
    passw = db.session.execute(db.select(UserData.password)).scalars()
    for i,j in enumerate(user):
        print(j)
    for i in passw:
        print(i)

@app.route("/login",methods =["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        cemail = db.session.execute(db.select(UserData.email).where(UserData.email==email)).scalar()
        rpassword = db.session.execute(db.select(UserData.password).where(UserData.email == email)).scalar()
        username = db.session.execute(db.select(UserData.username).where(UserData.email == email)).scalar()
        mobileno = db.session.execute(db.select(UserData.mobileno).where(UserData.email == email)).scalar()
        val = matchpass(email,cemail,rpassword,password)
        print(val)
        if val == True:
            return render_template ("user.html",user=username,email=email,mobileno=mobileno,Developer=param()['Developer'])
        else:
            return render_template ("login.html", content="true")
        # for i in user:
        #     print(1,i)
        #passa = db.get_or_404(UserData,password)
        #print("Email: ",user,"\n","Password: ",password)
        return redirect("terms.html")
    else:
        return render_template("login.html",content="false")

@app.route("/createaccount",methods =["POST","GET"])
def createacount():
    if request.method == "POST":
        user = UserData(
            email = request.form["email"],
            username=request.form["name"],
            password=request.form["password"],
            mobileno=request.form["mobile"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect("login")
    
    else:
        printUserandpass()
        return render_template("createaccount.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")
if __name__== "__main__":
    app.run(debug=True)