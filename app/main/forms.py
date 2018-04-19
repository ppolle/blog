from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email

class CreatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()])
	post = TextAreaField('Post Content')
	submit = SubmitField('Submit')

class CreateCommentForm(FlaskForm):
	name = StringField('Your Name',validators=[Required()])
	email = StringField('Your Email Address',validators=[Required(),Email()])
	comment = TextAreaField('Post Content',validators =[Required()])
	submit = SubmitField('Submit')