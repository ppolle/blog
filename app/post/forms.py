from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField
from wtforms.validators import Required,Email

class CreatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()])
	post = TextAreaField('Post Content')
	submit = SubmitField('Submit')