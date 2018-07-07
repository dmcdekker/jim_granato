from model import User, Work, connect_to_db, db
from server import app

def seed_data():
    """Create example data for the test database."""


    work_1 = Work(_class='music', _id='this_one', image='/static/images/jim_camera_small.jpg', title='xxxxxxxxx',
                  text='Something about this thingy do dah',  iframe='dmcdekker')


    db.session.add(work_1)
    db.session.commit()
        


