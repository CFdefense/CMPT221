"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        query = insert(User).values(request.form)
        '''
            f"""INSERT INTO "Users" ("FirstName", "LastName", "Email", "PhoneNumber", "Password") 
                VALUES 
                ('{request.form["FirstName"]}',
                '{request.form["LastName"]}', 
                '{request.form["Email"]}',
                '{request.form["PhoneNumber"]}',
                '{request.form["Password"]}');
            """
        '''
        db.session.execute(query)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
    # from request.form extract password and Email
        entered_pass = request.form["Password"]
        entered_email = request.form["Email"]

        # select password from users where Email == entered_email and compare to input password
        pass_query = select(User.Password).where(User.Email == entered_email)

        # return redirect if accepted to new page to be created for login
        user_pass = db.session.execute(pass_query).fetchone()

        # return to homepage/maybe send message of failure
        if user_pass[0] == entered_pass:
            return redirect(url_for('index'))
        else:
            # redirect to login
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/users')
def users():
    with app.app_context():
        # select users where the first name is Calista
        # stmt = select(User).where(User.FirstName == "Calista")

        # select all users
        stmt = select(User)
        all_users = db.session.execute(stmt)

        return render_template('users.html', users=all_users)
    
    return render_template('users.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

