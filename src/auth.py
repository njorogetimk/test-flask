from flask import Blueprint, jsonify, request
from src.database import Cow, CowSchema, db

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


cow_sch = CowSchema()
cows_sch = CowSchema(many=True)


@auth.get('/home')
def home():
    return jsonify({"msg":"welcome home"})


@auth.post('/register')
def register():
    tag = request.json.get('tag', '')
    breed = request.json.get('breed', '')

    if not tag or not breed:
        return jsonify({"msg", "missing info"}), 400
    
    chk = Cow.query.filter_by(tag=tag).first()

    if chk:
        return jsonify({"msg":"tag already taken"}), 400

    cow = Cow(tag=tag, breed=breed)
    db.session.add(cow)
    db.session.commit()

    return jsonify({
        "msg":"registered",
        "cow": cow_sch.dump(cow)
    }), 201


@auth.get('/cow/<id>')
def get_cow(id):
    cow = Cow.query.get(id)

    if not cow:
        return jsonify({"msg": "Wrong id!"}), 404
    
    return jsonify({"cow":cow_sch.dump(cow)})


@auth.get('/cows')
def get_cows():
    cows = Cow.query.all()

    return jsonify({"cows":cows_sch.dump(cows)})