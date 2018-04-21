from flask import Flask,render_template,request,redirect,url_for
from . import main
from .forms import CreateCommentForm
from ..models import Post,Comment
from .. import db
import markdown2 

# Views
@main.route('/')
def index():
	posts = Post.query.all()
	recentPosts = Post.query.order_by(Post.id.desc()).limit(6)
	title = 'Mhenga Petero'
	return render_template('index.html',title = title,posts = posts,recentPosts = recentPosts)

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
	postBody = markdown2.markdown(post.post,extras=["code-friendly", "fenced-code-blocks"])
	return render_template('single.html',post = post, commentForm = commentForm,title=title,blogComments = blogComments, postBody = postBody)

