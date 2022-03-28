from flask_sqlalchemy import SQLAlchemy

# creating the database and connecting to it.
DB = SQLAlchemy()


class User(DB.Model):
    # id
    id = DB.Column(DB.BigInteger, primary_key=True)
    # username
    username = DB.Column(DB.String, nullable=False)
    # tweets
    # tweets = (comes from DB.backref)

    def __repr__(self):
        return f"<User: {self.username}>"


class Tweet(DB.Model):
    # id
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text
    text = DB.Column(DB.Unicode(300))
    # user_id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    # user
    # Going to add an attribute to both tables (User and Tweet)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<Tweet: {self.text}>"
