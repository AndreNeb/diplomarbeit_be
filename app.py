from flask import Flask, render_template, request    # WSGI application

app = Flask(__name__)       # instance of class named; needed to look for resources
@app.route('/') # homepage
@app.route('/<name>') # run when name is entered in url
def index(name=None):
    return render_template('index.html', person=name)

with app.test_request_context('/', method='POST'):
    assert request.path == '/'
    assert request.method == 'POST'