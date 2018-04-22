from flask import Flask,render_template,request,redirect,url_for,flash
from . import main
from .forms import CreateCommentForm,AddSubscriberForm
from ..models import Post,Comment,Subscribe
from .. import db
import markdown2 
from ..email import mail_message

# Views
@main.route('/',methods = ['GET','POST'])
def index():
	posts = Post.query.all()
	recentPosts = Post.query.order_by(Post.id.desc()).limit(6)

	subscribeForm = AddSubscriberForm()

	if subscribeForm.validate_on_submit():
		addSubscriber = Subscribe(name = subscribeForm.name.data, email = subscribeForm.email.data)
		db.session.add(addSubscriber)
		db.session.commit()
		flash(f'Thank you {subscribeForm.name.data} for subscribing to my blog. A confirmatio email will be sent to you shortly')
		mail_message('Hello There New Subscriber','emails/subscribe',addSubscriber.email,addSubscriber = addSubscriber)
		return redirect(url_for('main.index'))

	title = 'Mhenga Petero'
	for post in posts:
		postBody = markdown2.markdown(post.post,extras=["code-friendly", "fenced-code-blocks"])
	breadcrumb = "Blog"
	return render_template('index.html',title = title,posts = posts,recentPosts = recentPosts,subscribeForm = subscribeForm,postBody = postBody,breadcrumb= breadcrumb)

@main.route('/blog/single/<int:id>',methods = ['GET','POST'])
def single(id):
	commentForm = CreateCommentForm()
	post = Post.query.get(id)
	blogComments = Comment.query.filter_by(post_id = id).all()
	recentPosts = Post.query.order_by(Post.id.desc()).limit(4)

	if commentForm.validate_on_submit():
		createComment = Comment(comment = commentForm.comment.data,name = commentForm.name.data,email = commentForm.email.data,post_id = id)
		
		db.session.add(createComment)
		db.session.commit()

		flash(f'Success! Thank you for commenting')
		return redirect(url_for('main.single',id = id))
	
	title = post.title
	breadcrumb = "Blog"
	postBody = markdown2.markdown(post.post,extras=["code-friendly", "fenced-code-blocks"])
	return render_template('single.html',post = post, commentForm = commentForm,title=title,blogComments = blogComments, postBody = postBody,recentPosts = recentPosts, breadcrumb = breadcrumb)

