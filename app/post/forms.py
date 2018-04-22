from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FileField
from wtforms.validators import Required,Email

class CreatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()],default = 'Post Title',)
	post = TextAreaField('Post Content',default = 'Post Content')
	image = FileField('Post Image',validators = [Required()])
	submit = SubmitField('Submit')

class UpdatePostForm(FlaskForm):
	title = StringField('Post title',validators=[Required()])
	post = TextAreaField('Post Content')
	submit = SubmitField('Update')