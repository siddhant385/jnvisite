from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
with app.app_context():
    db.create_all()


def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")


"""
<!DOCTYPE html>
<html>
	<head>
		<script>
		
			// Function to check Whether both passwords
			// is same or not.
			function checkPassword(form) {
				password1 = form.password1.value;
				password2 = form.password2.value;

				// If password not entered
				if (password1 == '')
					alert ("Please enter Password");
					
				// If confirm password not entered
				else if (password2 == '')
					alert ("Please enter confirm password");
					
				// If Not same return False.	
				else if (password1 != password2) {
					alert ("\nPassword did not match: Please try again...")
					return false;
				}

				// If same return True.
				else{
					alert("Password Match: Welcome to GeeksforGeeks!")
					return true;
				}
			}
		</script>
		<style>
			.gfg {
				font-size:40px;
				color:green;
				font-weight:bold;
				text-align:center;
			}
			.geeks {
				font-size:17px;
				text-align:center;
				margin-bottom:20px;
			}
		</style>
	</head>
	<body>
		<div class = "gfg">GeeksforGeeks</div>
		<div class = "geeks">A computer science portal for geeks</div>
		<form onSubmit = "return checkPassword(this)">
		<table border = 1 align = "center">
			<tr>
				<!-- Enter Username -->
				<td>Username:</td>
				<td><input type = text name = name size = 25</td>
			</tr>
			<tr>
				<!-- Enter Password. -->
				<td>Password:</td>
				<td><input type = password name = password1 size = 25</td>
			</tr>
			<tr>
				<!-- To Confirm Password. -->
				<td>Confirm Password:</td>
				<td><input type = password name = password2 size = 25></td>
			</tr>
			<tr>
				<td colspan = 2 align = right>
				<input type = submit value = "Submit"></td>
			</tr>
		</table>
		</form>
	</body>
</html>					

"""