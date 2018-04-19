from flask import Blueprint
main = Blueprint('post',__name__)
from . import views,forms