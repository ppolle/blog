from . import db
from . import login_manager
from flask_login import UserMixin


class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key = True)
	post = db.Column(db.String(255))
	comments = db.relationship('Comment',backref = 'role',lazy = 'dynamic')
	
	def __repr__(self):
		return f'User {self.post}'