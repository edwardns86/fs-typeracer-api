from flask import Flask,  jsonify , request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://primaryuser:password@localhost:5432/fstyperacer'
app.secret_key='super super secret key'
db = SQLAlchemy(app) 
migrate=Migrate(app, db)

CORS(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    scores = db.relationship('Score', backref='user', lazy=True )
    

class Excerpt(db.Model):
    __tablename__ = 'excerpts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    scores = db.relationship('Score', backref='excerpt', lazy=True )
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in     self.__table__.columns}

    

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    wpm = db.Column(db.Integer)
    errors = db.Column(db.Integer)
    scores_count= db.Column(db.String)
    excerpt_id = db.Column(db.Integer, db.ForeignKey('excerpts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('excerpts.id'))

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in  self.__table__.columns}
    
    

@app.route('/')
def root():
    return jsonify(['Hello', 'World'])

@app.route('/scores', methods=['GET','POST'])
def create():
    
    if request.method == 'POST':
        dt = request.get_json()
        score = Score(
        user_id = 1 , 
        time=dt['time'], 
        wpm=dt['wpm'], 
        errors=dt['errorCount'], 
        excerpt_id= dt[('excerpt_id')]
        scores_count= +1
        )
        
        db.session.add(score)
        
        db.session.commit()
        jsonized_excerpt_objects_list = []
        jsonized_excerpt_objects_list.append(score.as_dict())
        print('object', jsonify(jsonized_excerpt_objects_list))
        return jsonify(jsonized_excerpt_objects_list)

@app.route('/excerpts', methods= ['GET', 'POST'])
def getexcerpts():
    excerpts = Excerpt.query.all()
    jsonized_excerpt_objects_list = []
    for excerpt in excerpts:
        jsonized_excerpt_objects_list.append(excerpt.as_dict())

    return jsonify(jsonized_excerpt_objects_list)

if __name__ == "__main__":
    app.run(debug=True)