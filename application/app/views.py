from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('errorpage.html', error_code='403'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpage.html', error_code='404'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errorpage.html', error_code='500'), 500 

