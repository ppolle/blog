from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CreatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()])
	post = TextAreaField('Post Content', validators=[Required()])
	submit = SubmitField('Submit')