"""Models and database functions for HB project."""

from flask import Flask

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=False, primary_key=True)
    email = db.Column(db.String(64), nullable=True, unique=True)
    password = db.Column(db.String(64), nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""



        return "<User: {email}\t".format(email=self.email, city=self.city)
                                                                        


class Work(db.Model):

    __tablename__ = "works"
    
    work_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    html_class = db.Column(db.String(64), nullable=True)
    html_id = db.Column(db.String(64), nullable=True)
    title = db.Column(db.String(64), nullable=True)
    text = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(64), nullable=True)
    iframe = db.Column(db.String(64), nullable=True)


    
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Work ID: {work_id}\n{html_class} {html_id} {title} {text} {image} {iframe} >".format(id=self.work_id,
                                                                    _class=self.html_class,
                                                                    _id=self.html_id,
                                                                    image=self.image,
                                                                    title=self.title,
                                                                    text= self.text, 
                                                                    iframe=self.iframe)


#########################################################################################
# Helper functions

def connect_to_db(app, db_uri="postgresql:///jimg"):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interis_actively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print ("Connected to DB")


