from jinja2 import StrictUndefined

from flask import Flask, render_template, flash, redirect, session
from model import connect_to_db, db, User, Work

app = Flask(__name__)

app.secret_key = "jimg_app"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""
    return render_template('homepage.html')


@app.route('/work')
def user_list():
    """Show list of all work"""

    works = Work.query.all()

    return render_template('work.html', works=works)


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("You are now logged in")
    return redirect("/work")


@app.route('/logout')
def logout():
    """Log out."""

    del session['user_id']
    flash('You are now logged out')

    return redirect('/')


if __name__ == "__main__":


    app.debug = False

    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # disable intercept redirects
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    connect_to_db(app)


    app.run(host="0.0.0.0")
