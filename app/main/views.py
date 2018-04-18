from flask import render_template,request,redirect,url_for
from . import main
from .forms import CreatePostForm
from ..models import Post,Comment
from .. import db
# Views
@main.route('/')
def index():
	title = 'Flask Base'
	return render_template('index.html',title = title)

@main.route('/admin/create_post',methods = ['GET','POST'])
def new_post():
	form = CreatePostForm()

	if form.validate_on_submit():
		title = form.title.data 
		post =  form.post.data

		db.session.add_all([title,post])
		db.session.commit()
		
		return redirect(url_for('.index',title =  title))

		title = "Create New Post"
		return render_template('posts/create.html',form =form)