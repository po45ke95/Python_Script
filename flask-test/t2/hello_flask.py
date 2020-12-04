from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello flask'

@app.route('/123/<user>')
def index(user):
    return render_template('abc.html', user_template=user)

if __name__ == '__main__':
    app.debut = True
    app.run()