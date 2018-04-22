from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField
from wtforms.validators import Required,Email

class CreatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()])
	post = TextAreaField('Post Content')
	image = FileField('Post Image',validators = [Required()])
	submit = SubmitField('Submit')

class UpdatePostForm(FlaskForm):
	title = StringField('Update Post title',validators=[Required()])
	post = TextAreaField('Update Post Content')
	image = FileField('Update Post Image',validators = [Required()])
	submit = SubmitField('Update')