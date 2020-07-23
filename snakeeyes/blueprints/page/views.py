from flask import Blueprint , render_template

page = Blueprint('name',__name__,static_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

@page.route('/terms')
def terms():
    return render_template('name/terms.html')