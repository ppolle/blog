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

