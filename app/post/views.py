from flask import Flask,render_template,request,redirect,url_for
from . import post
from .forms import CreatePostForm
from ..models import Post,Comment
from .. import db

@post.route('/admin/create_post',methods = ['GET','POST'])
def new_post():
	form = CreatePostForm()

	if form.validate_on_submit():
		 
		blogpost =  Post(title = form.title.data,post = form.post.data)


		db.session.add(blogpost)
		db.session.commit()
		
		
		return redirect(url_for('main.index'))

	title = "Create New Post"
	return render_template('post/create.html',form =form, title= title)