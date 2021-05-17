# SQLAlchemy Apartments

## Goals

1. Get a backend server up and running with flask
1. Have our flask server communicating with our postgres DB
1. Create CRUD functions that communicate with the backend (no routes and controllers yet) (no req,res yet just functions)

- you are only going to create 1 route that will invoke a function
- this means that for each function, you should write the function, test that it works via postman or thunderclient and if it does then comment it out when you move onto the next function.
- you will submit your functions either in the application.py or create a separate file for each part with those functions included

## Setup Tips

<details>

1. Create the python3 virtual environment
   - python3 -m venv virtual-environment
1. Activate your virtual environment
   - source virtual-environment/bin/activate
   - add virtual-environment to your git ignore
1. WHILE YOUR VIRTUAL ENVIRONMENT IS ACTIVATED

   - pip3 install alembic
   - alembic init migrations
   - pip3 install python-dotenv
   - update the migrations/env.py

   ```
   from dotenv import load_dotenv
   import os
   load_dotenv()
   db_url = os.environ.get("DATABASE_URL")


   config = context.config
   config.set_main_option('sqlalchemy.url', db_url)
   ```

1. Create a .env at the root of the directory
   ```
   DATABASE_URL=postgresql://localhost:5432/sqlalchemy_apartments
   ```
1. pip3 install psycopg2
1. Create your database via psql and name it sqlalchemy_apartments
1. alembic upgrade head (this doesn't do anything, but if it runs w/o errors you know you're good up til this point)
</details>

## Migration tips

<details>

1. alembic revision -m create-tableName
1. go into the created migration file
1. put into upgrade function:

```
EXAMPLE
  op.create_table(
    'tableName',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('email', sa.String, nullable=False, unique=True),
    sa.Column('password', sa.String, nullable=False)
  )
```

1. alembic upgrade head
1. optionally put into downgrade: op.drop_table('users') (this will undo the table if you run alembic downgrade -1)
1. confirm table in psql
</details>

## Models tips

<details>

1. pip3 install flask_sqlalchemy
1. at the root, make models.py and add

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

1. add our model class

```
 class User(db.Model):
    __tablename__ = users
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
```

</details>

## Tables/Models Needed

1. Apartment Model

   - id
   - name (String)
   - units (Integer)
   - owner_id (Integer) (foreign key owners.id)

1. Owner Model
   - id
   - name (String)
   - age (Integer)
   - apartments (relationship with apartments )

## Part 1

- Insert the following owners
- William - age 29
- Jane - age 43
- Yuki - Age 67

- Insert the following apartments
- Archstone - 20 units
- Zenith Hills - 10 units
- Willowspring - 30 units

## Part 2

- Print all the data in the owners table.

- Print all the data in the properties table.

- Print just the names of all owners.

- Print the names and ages of all owners who are older than 30.

- Look up William, save him to a variable, and print it

- Look up archstone, save it to a variable, and print it.

- Change Jane's age to 30.

- Change Jane's name to Janet.

## Part 3

- Associate each property with an owner:
- Archstone - belongs to Yuki
- Zenith Hills - belongs to Yuki
- Willowspring - belongs to Jane

- Print all the properties that are owned by Yuki.

- Print the count (length) of how many properties Yuki owns.

- Find Willowspring's owner and print their name.

- Change Willowspring so that is now owned by Yuki.

- Print the names of the people who own properties that have 20 units or more
