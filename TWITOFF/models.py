from flask_sqlalchemy import SQLAlchemy

''' sql alchemy models for twitoff '''


DB = SQLAlchemy()

class User(DB.Model):
    ''' Twitter users that we pull and analyze '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets"""

    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger,DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User',backref=DB.backref('tweet',lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)


def generate(name,tweet):

    u1 = User(name=name)
    t1 = Tweet(text=tweet)
    DB.session.add(u1)
    DB.session.add(t1)
    DB.session.commit()
    return "Generated a tweet by " + str(u1) + "with the tweet: " + str(tweet)

#tweet_generator("Gabe","was good its ya boy")
