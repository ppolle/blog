from flask import Flask,render_template,request,redirect,url_for
from . import main
from .forms import CreatePostForm,CreateCommentForm
from ..models import Post,Comment
from .. import db

# Views
@main.route('/')
def index():
	posts = Post.query.all()
	title = 'Flask Base'
	return render_template('index.html',title = title,posts = posts)

@main.route('/blog/single/<int:id>',methods = ['GET','POST'])
def single(id):
	commentForm = CreateCommentForm()
	post = Post.query.get(id)
	blogComments = Comment.query.filter_by(post_id = id).all()

	if commentForm.validate_on_submit():
		createComment = Comment(comment = commentForm.comment.data,name = commentForm.name.data,email = commentForm.email.data,post_id = id)
		
		db.session.add(createComment)
		db.session.commit()


		return redirect(url_for('main.single',id = id))
	
	title = post.title
	return render_template('single.html',post = post, commentForm = commentForm,title=title,blogComments = blogComments)




@main.route('/admin/create_post',methods = ['GET','POST'])
def new_post():
	form = CreatePostForm()

	if form.validate_on_submit():
		 
		blogpost =  Post(title = form.title.data,post = form.post.data)


		db.session.add(blogpost)
		db.session.commit()
		
		
		return redirect(url_for('main.index'))

	title = "Create New Post"
	return render_template('post/create.html',form =form, title= title)