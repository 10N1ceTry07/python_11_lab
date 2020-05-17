from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.main.classes.base_camping import BaseCamping
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartBaseCamping(BaseCamping, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    producer = db.Column(db.String(64), unique=False)
    things_type = db.Column(db.Enum, unique=False)
    weight_in_kilo = db.Column(db.Float, unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)
    connection_protocol = db.Column(db.String(32), unique=False)
    data_transfer_amount = db.Column(db.Float, unique=False)

    def __init__(self, name, producer, things_type, weight_in_kilo, price_in_uah,
                 availability_of_boat=None, connection_protocol='telnet', data_transfer_amount=0.0):
        super().__init__(name, producer, things_type, weight_in_kilo, price_in_uah)
        self.connection_protocol = connection_protocol
        self.data_transfer_amount = data_transfer_amount


class SmartBaseCampingSchema(ma.Schema):
    class Meta:
        fields = ('name', 'producer', 'things_type', 'weight_in_kilo',
                  'price_in_uah', 'connection_protocol', 'data_transfer_amount')


smart_base_camping_schema = SmartBaseCampingSchema()
smart_base_camping_schema = SmartBaseCampingSchema(many=True)


@app.route("/smart_base_camping", methods=["POST"])
def add_smart_base_camping():
    smart_base_camping = SmartBaseCamping(request.json['name'],
                                          request.json['producer'],
                                          request.json['things_type'],
                                          request.json['weight_in_kilo'],
                                          request.json['price_in_uah'],
                                          request.json['connection_protocol'],
                                          request.json['data_transfer_amount'])
    db.session.add(smart_base_camping)
    db.session.commit()
    return smart_base_camping_schema.jsonify(smart_base_camping)


@app.route("/smart_base_camping", methods=["GET"])
def get_smart_base_camping():
    all_smart_base_camping = SmartBaseCamping.query.all()
    result = smart_base_camping_schema.dump(all_smart_base_camping)
    return jsonify({'smart_base_camping': result})


@app.route("/smart_base_camping/<id>", methods=["GET"])
def smart_base_camping_detail(id):
    smart_base_camping = SmartBaseCamping.query.get(id)
    if not smart_base_camping:
        abort(404)
        return smart_base_camping_schema.jsonify(smart_base_camping)


@app.route("/smart_base_camping/<id>", methods=["PUT"])
def smart_base_camping_update(id):
    smart_base_camping = SmartBaseCamping.query.get(id)
    if not smart_base_camping:
        abort(404)
    old_smart_base_camping = copy.deepcopy(smart_base_camping)
    smart_base_camping.name = request.json['name']
    smart_base_camping.producer = request.json['producer']
    smart_base_camping.things_type = request.json['things_type']
    smart_base_camping.weight_in_kilo = request.json['weight_in_kilo']
    smart_base_camping.price_in_uah = request.json['price_in_uah']
    smart_base_camping.connection_protocol = request.json['connection_protocol']
    smart_base_camping.data_transfer_amount = request.json['data_transfer_amount']
    db.session.commit()
    return smart_base_camping_schema.jsonify(old_smart_base_camping)


@app.route("/smart_base_camping/<id>", methods=["DELETE"])
def smart_base_camping_delete(id):
    smart_base_camping = SmartBaseCamping.query.get(id)
    if not smart_base_camping:
        abort(404)
    db.session.delete(smart_base_camping)
    db.session.commit()
    return smart_base_camping_schema.jsonify(smart_base_camping)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
