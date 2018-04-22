from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime


class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(255))
	post = db.Column(db.String)
	image = db.Column(db.String)
	created_at = db.Column(db.DateTime,default = datetime.utcnow)
	comments = db.relationship('Comment',backref = 'role',lazy = 'dynamic')

	def __repr__(self):
		return f'User {self.post}'

class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key = True)
	comment = db.Column(db.String)
	name = db.Column(db.String(255))
	email = db.Column(db.String)
	post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

	def __repr__(self):
		return f'User {self.comment}'
