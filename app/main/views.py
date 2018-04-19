from flask import render_template,request,redirect,url_for
from . import main
from .forms import CreatePostForm
from ..models import Post,Comment
from .. import db
# Views
@main.route('/')
def index():
	posts = Post.query.all()
	title = 'Flask Base'
	return render_template('index.html',title = title,posts = posts)

@main.route('/blog/single/<int:id>')
def single(id):
	pass



@main.route('/admin/create_post',methods = ['GET','POST'])
def new_post():
	form = CreatePostForm()

	if form.validate_on_submit():
		 
		blogpost =  Post(title = form.title.data,post = form.post.data)


		db.session.add(blogpost)
		db.session.commit()
		
		
		return redirect(url_for('main.index'))

	title = "Create New Post"
	return render_template('posts/create.html',form =form, title= title)