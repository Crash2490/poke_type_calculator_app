from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList


# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/crash/PycharmProjects/pokemon-api/pokemon.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type1 = db.Column(db.String)
    type2 = db.Column(db.String)
    sprite = db.Column(db.String)

    def __str__(self):
        return "id = {}, name = {}, type1 = {}, type2 = {}, sprite = {}".format(self.id, self.name, self.type1, self.type2, self.sprite)
# Create the table

db.create_all()

# Create data abstraction layer
class PokemonSchema(Schema):
    class Meta:
        type_ = 'pokemon'
        self_view = 'pokemon_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'pokemon_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    type1 = fields.Str()
    type2 = fields.Str()
    sprite = fields.Str()

# Create resource managers and endpoints
class PokemonMany(ResourceList):
    schema = PokemonSchema
    data_layer = {'session': db.session,
                  'model': Pokemon}

class PokemonOne(ResourceDetail):
    schema = PokemonSchema
    data_layer = {'session': db.session,
                  'model': Pokemon}

api = Api(app)
api.route(PokemonMany, 'pokemon_many', '/pokemon')
api.route(PokemonOne, 'pokemon_one', '/pokemon/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)


# curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"pokemon", "attributes":{"name":"Pidgeot", "type1":"Normal", "type2":"Flying"}}}' http://localhost:5000/pokemon