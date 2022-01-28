from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)


class Item(db.Model):
    id= db.Column(db.Integer(),primary_key=True)
    name= db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(),nullable=False,unique=True)
    description=db.Column(db.String(),nullable=False)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('homepage.html')

@app.route('/market')
def market_page():
    return render_template('market.html')

