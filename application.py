from flask import Flask
from flask import request, jsonify, json


app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

def db_test():
    # Part1
    
    # inser the owners
    # owner = models.Owner(
    #     name="William",
    #     age=29
    # )
    # owner2= models.Owner(
    #     name='Jane',
    #     age='43'
    # )
    # owner3= models.Owner(
    #     name='Yuku',
    #     age='67'
    # )
   
    # models.db.session.add(owner2)
    # models.db.session.add(owner3)
    
    # inser the apartments
    # apartment1 = models.Apartment(
    #     name='Archstone',
    #     units=20,    
    # )
    # apartment2 = models.Apartment(
    #     name='Zenith Hills',
    #     units=10,
    # )
    # apartment3 = models.Apartment(
    #     name='Willowspring',
    #     units=30,
    # )
    # models.db.session.add(apartment1)
    # models.db.session.add(apartment2)
    # models.db.session.add(apartment3)
    # models.db.session.commit()
    # return 'ok'
    
    
    # Part2
    
    # Print all the data in the owners table
    # owners = models.Owner.query.all()
    # print(owners[0].name)
    # for i in owners:
    #     print(i.name, i.age)
        
    
    # Print all the data in the properties table.
    
    # apartments = models.Apartment.query.all()
    # for i in apartments:
    #     print(i.name)
    
    # Print just the names of all owners.
    # owners_names = models.Owner.query.all()
    # for i in owners_names:
    #     print(i.name)
    
    
    # Print the names and ages of all owners who are older than 30
    # older_than_30 = models.Owner.query.filter(models.Owner.age>30).all()
    
    # for i in older_than_30:
    #     print(i.name, i.age)
    
    # Look up William, save him to a variable, and print it
    # william = models.Owner.query.filter_by(name="William").first()
    # print(william.name)
    
    # Look up archstone, save it to a variable, and print it
    # archstone = models.Apartment.query.filter_by(name='Archstone').first()
    # print(archstone.name)
    
    # Change Jane's age to 30.
    # jane = models.Owner.query.filter_by(name="Jane").first()
    # jane.age = 30
    # models.db.session.add(jane)
    # models.db.session.commit()
    
    # Change Jane's name to Janet.
    # jane = models.Owner.query.filter_by(name='Jane').first()
    # jane.name = 'Janet'
    # models.db.session.add(jane)
    # models.db.session.commit()
    
    return 'ok'
   
    # Part1
    
    # inser the owners
app.route('/db_test', methods=["GET"])(db_test)


@app.route('/create', methods=["POST"])
def create_owner():
    create_owner = models.Owner(
         name = request.json["name"],
         age = request.json["age"]
    )    
  
    
    models.db.session.add(create_owner)   
    models.db.session.commit()
    print(create_owner)
    return jsonify(create_owner.to_json())

# app.route('owner/create',methods=["POST"],create_owner)    

@app.route('/create/apartment', methods=["POST"])
def create_apartment():
    apartment = models.Apartment(
        name=request.json["name"],
        units=request.json["units"]
    )
    print(apartment)
    models.db.session.add(apartment)   
    models.db.session.commit()
    return jsonify(apartment.to_json())

@app.route('/owner/get-one', methods=["GET"])
def read_one_owner():
    owners = models.Owner.query.filter_by(id=request.args.get('id')).first()

    print(owners.name)

    return 'ok'
# app.route('/owner/get-one', methods=["GET"])(read_one_owner)

#

@app.route('/owner/update', methods=["PUT"])
def update_owner():
    owner = models.Owner.query.filter_by(id=request.args.get('id')).first()
    owner.name = request.json['name']
    owner.age = request.json['age']
    
    models.db.session.add(owner)
    models.db.session.commit()
    return jsonify(owner.to_json())


# @app.route('/owner/delete', methods=["DELETE"])
def delete_owner():

    owner = models.Owner.query.filter_by(id=request.args.get('id', type=int)).first()

    models.db.session.delete(owner)
    models.db.session.commit()

    return 'deleted'


app.route('/owner/delete', methods=["DELETE"])(delete_owner)

@app.route('/getAll', methods=["GET"])
def get_all():
    all_owners= models.Owner.query.all()
    
    for i in all_owners:
        print(i.name, i.age)
    return 'ok'

@app.route('/getAllAparts', methods=["GET"])
def get_apartments():
    all_aps = models.Apartment.query.all()
    for i in all_aps:
        print(i.name, i.units)
    return 'ok'


@app.route('/get/name', methods=["GET"])
def get_by_name():
    name = models.Owner.query.filter_by(name=request.args.get("name")).first()
    print(name)

#Aossiaontions

# add this in postman
# http://localhost:5000/associate?owner_id=3&apartment=1
@app.route('/associate', methods=["POST"])
def associate():
    try:
        owner = models.Owner.query.filter_by(id=request.args.get('owner_id', type=int)).first()

        apartment = models.Apartment.query.filter_by(id=request.args.get('apartment_id', type=int)).first()

        owner.owner_apt.append(apartment)

        models.db.session.add(owner)
        models.db.session.commit()

        return jsonify({'owner' : owner.to_json(), 'apartment' : apartment.to_json()})


    except Exception as e:
        print(e)
        return jsonify({"error" : f'{e}'})

def 




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)