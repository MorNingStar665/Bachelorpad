from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("test.html")

@views.route('/Plans')
def Plans():
    return render_template("plans.html")
