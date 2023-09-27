"""Flask app for Cupcakes"""
from flask import Flask,render_template, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, Cupcake
WTF_CSRF_SECRET_KEY='abc'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abc'
connect_db(app)
#db.init_app(app)   
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/api/cupcakes', methods=['POST', 'GET'])
def cupcakes_page():
    if request.method == 'POST':
        body=request.json
        cupcake = Cupcake(  
            flavor = body['flavor'],
            size = body['size'],
            rating = body['rating'],
            image = body['image'],
            
        )
        db.session.add(cupcake) 
        db.session.commit()
        return jsonify(cupcake=cupcake.to_dict()) 

    else:
        cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
        return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE', 'GET', 'PATCH'])
def cupcakehandle(id): 
    if request.method == 'GET':
        cupcake = Cupcake.query.get_or_404(id)
        
        return jsonify(cupcake=cupcake.to_dict()) 
    elif request.method == 'DELETE':
        cupcake = Cupcake.query.get_or_404(id)

        db.session.delete(cupcake)
        db.session.commit()

        return jsonify(message="Deleted")




