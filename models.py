from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Apartment(db.Model):
    __tablename__ = 'apartments'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    units=db.Column(db.Integer)
    # owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    def to_json(self):
        return {
            "name":self.name,
            "units":self.units,
            
        }

        
class Owner(db.Model):
    __tablename__ = 'owners'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    age=db.Column(db.Integer)
    owner_apt = db.relationship('Apartment')
    # owner_apt = db.relationship('Apartment')
    def to_json(self):
        return {
            "name":self.name,
            "age":self.age,
            
        }