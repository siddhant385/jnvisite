

def matchpass(email,cemail,rpassword,password):
    print(password,rpassword)
    if password == rpassword:
        return True
    else:
        return False

# usera = db.session.execute(db.select(UserData.email).where(UserData.email==email)).scalars()
# rpassword = db.session.execute(db.select(UserData.password).where(UserData.email == email)).scalar()
# user = db.session.execute(db.select(UserData.password).order_by(UserData.email)).scalars()