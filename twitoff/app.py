from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    # Tell our app where to find our database
    # "registering" our database with the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route("/")
    def home():
        # query the database for all users
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route("/reset")
    def reset():
        # Drop our DB tables
        DB.drop_all()
        # Create tables according to the classes in models.py
        DB.create_all()
        return render_template('base.html', title='Reset DB')

    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='Ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='Julian')
        DB.session.add(julian)
        tweet1 = Tweet(id=1, text='Ryans tweet', user=ryan)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text='Julians tweet', user=julian)
        DB.session.add(tweet2)
        DB.session.commit()
        return render_template('base.html', title='Populate')

    return app
