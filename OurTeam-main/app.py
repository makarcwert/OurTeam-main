from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///team.db'
#db = SQLAlchemy(app)

#class Members(db.Model):
    #id = db.Column(db.Integer, primary_key=True)

#@app.route('/test')
@app.route('/')  #маршрут для главной страницы 

def hello():
    return 'Скоро....'


if __name__ == '__main__':
    app.run()