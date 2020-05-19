from app import db
from datetime import datetime

class Radio(db.Model):
	id= db.Column(db.Integer, primary_key = True)
	name= db.Column(db.String(80))
	stream = db.Column(db.String(100),unique= True)
	img= db.Column(db.String(10))
	site = db.Column(db.String(30))
	tag_id= db.Column(db.Integer, db.ForeignKey('tag.id'))

	def __init__(self, *args, **kwargs):
		super(Radio, self).__init__(*args, **kwargs)

	def __repr__ (self):
		return 'Radio id: {}, name: {}'.format (self.id, self.name)

class Tag(db.Model):
	id=db.Column(db.Integer, primary_key = True)
	name= db.Column(db.String(80))
	radio = db.relationship('Radio', backref = 'tag', lazy = 'dynamic')

	def __init__(self, arg):
		super(Tag, self).__init__(*args, **kwargs)

	def __repr__ (self):
		return 'Tag id: {}, name: {}'.format (self.id, self.name)


		

class User(db.Model):
	id= db.Column(db.Integer, primary_key = True)
	username= db.Column(db.String(25), unique= True)
	password_hash= db.Column(db.String(25))
	msg = db.relationship('Message', backref = 'author', lazy = 'dynamic')

	def __init__(self):
		super(User, self).__init__(*args, **kwargs)

	def __repr__(self):
		return 'User id: {}, username: {}'.format(self.id , self.username)

class Message(db.Model):
	id= db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(500))
	timestamp = db.Column(db.Integer, index = True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self):
		super(User, self).__init__(*args, **kwargs)

	def __repr__(self):
		return 'Post body {}'.format(self.body)
