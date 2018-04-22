from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email


class CreateCommentForm(FlaskForm):
	name = StringField('Name',validators=[Required()],default = 'Name')
	email = StringField('Email',validators=[Required(),Email()],default = 'Email')
	comment = TextAreaField('Comment',validators =[Required()],default = 'Message...')
	submit = SubmitField('Submit')

class AddSubscriberForm(FlaskForm):
	name = StringField('Your Name',validators=[Required()])
	email = StringField('Your Email Address',validators=[Required(),Email()])
	submit = SubmitField('Subscribe')