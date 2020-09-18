from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList
from weakness import weakness

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/crash/PycharmProjects/pokemon-api/pokemon.db'
db = SQLAlchemy(app)


# Define a class for the Artist table
class Pokemon(db.Model):
    """Pocket Monster"""

    id = db.Column(db.Integer, primary_key=True)
    dex_num = db.Column(db.Integer)
    name = db.Column(db.String)
    type1 = db.Column(db.String)
    type2 = db.Column(db.String)
    sprite = db.Column(db.String)
    type_values = db.Column(db.JSON)


    def __str__(self):
        return "id = {}, dex_num = {}, name = {}, type1 = {}, type2 = {}, sprite = {}, type_values = {}".format(self.id, self.dex_num, self.name, self.type1, self.type2, self.sprite, self.type_values)

    def _dict(self):
        return {"id": self.id, "dex_num": self.dex_num, "name": self.name, "type1": self.type1, "type2": self.type2,"sprite": self.sprite, "type_values": self.type_values}

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
    dex_num = fields.Integer()
    name = fields.Str(required=True)
    type1 = fields.Str()
    type2 = fields.Str()
    sprite = fields.Str()
    type_values = fields.Dict()

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


@app.route("/pokemon/<string:name>")
def user_detail(name):
    battletype = request.args.get('battletype')

    schema = PokemonSchema()
    p = Pokemon.query.filter_by(name=name).first()
    pdict = schema.dump(p).data

    type1 = pdict['data']['attributes']['type1']
    type2 = pdict['data']['attributes']['type2']
    pdict['data']['attributes']['inver_type_vals'] = weakness(battletype, type1, type2)
    return pdict


@app.route("/<string:type1>/<string:type2>")
def get_weakness(type1, type2):
    battletype = request.args.get('battletype')
    if type2 == 'none':
        type2 = None
    return weakness(battletype, type1, type2)

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
