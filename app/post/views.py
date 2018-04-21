from flask import Flask,render_template,request,redirect,url_for
from . import post
from .forms import CreatePostForm,UpdatePostForm
from ..models import Post,Comment
from .. import db

@post.route('/create_post',methods = ['GET','POST'])
def new_post():
	form = CreatePostForm()

	if form.validate_on_submit():
		 
		blogpost =  Post(title = form.title.data,post = form.post.data)


		db.session.add(blogpost)
		db.session.commit()
		
		post = Post.query.order_by(Post.id.desc()).first()
		return redirect(url_for('post.single',id = post.id))

	title = "Create New Post"
	return render_template('post/create.html',form =form, title= title)

@post.route('/single/<int:id>')
def single(id):
	post = Post.query.get(id)
	comments = Comment.query.filter_by(post_id = id).all()

	title = post.title
	return render_template('post/single.html',title=title,post=post,comments = comments)

@post.route('/index')
def index():
	posts = Post.query.all()

	title = 'All Posts'
	return render_template('post/index.html',title = title, posts = posts)

@post.route('deleteComment/<int:id>')
def delete_comment(id):
	comment = Comment.query.get(id)
	db.session.delete(comment)
	db.session.commit()

	return redirect(url_for('post.single',id = comment.post_id))

@post.route('deletePost/<int:id>')
def delete_post(id):
	post = Post.query.get(id)
	db.session.delete(post)
	db.session.commit()

	return redirect(url_for('post.index'))

@post.route('update/<int:id>')
def update(id):
	postForm = UpdatePostForm()
	post = Post.query.get(id)

	if postForm.validate_on_submit():
		post.update(title = postForm.title.data, post = postForm.post.data)
		db.session.commit()

		return redirect(url_for('post.single',id = id))

	postForm.title.data = post.title
	postForm.post.data = post.post

	return render_template('update.html',postForm = postForm)
