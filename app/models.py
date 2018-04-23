from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager


class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(255))
	post = db.Column(db.String)
	image = db.Column(db.String)
	created_at = db.Column(db.DateTime,default = datetime.utcnow)
	comments = db.relationship('Comment',backref = 'role',lazy = 'dynamic')

	def __repr__(self):
		return f'Post {self.post}'

class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key = True)
	comment = db.Column(db.String)
	name = db.Column(db.String(255))
	email = db.Column(db.String)
	post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

	def __repr__(self):
		return f'Comment {self.comment}'

class Subscribe(db.Model):
	__tablename__ = 'subscribers'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))

	def __repr__(self):
		return f'Subscriber {self.name}'

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	pass_secure = db.Column(db.String(255))

	@property
	def password(self):
		raise AttributeError('You cannot read the password attribute')
	@password.setter
	def password(self, password):
		self.pass_secure = generate_password_hash(password)


	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	def __repr__(self):
		return f'User {self.name}'


