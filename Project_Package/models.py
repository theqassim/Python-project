from datetime import datetime
from Project_Package import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='profile.png')
    password = db.Column(db.String(60), nullable=False)
    videos = db.relationship('Videos', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.fname}','{self.lname}' ,'{self.username}' , '{self.email}', '{self.image_file}')"

class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(50), nullable=False, default='thumbnail-default.jpg')
    slug = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

    def __repr__(self):
        return f"Videos('{self.title}', '{self.date_posted}')"

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    icon = db.Column(db.String(50), nullable=False, default='video-playlist.png')
    videos = db.relationship('Videos', backref='playlist_name', lazy=True)

    def __repr__(self):
        return f"Playlist('{self.title}')"
