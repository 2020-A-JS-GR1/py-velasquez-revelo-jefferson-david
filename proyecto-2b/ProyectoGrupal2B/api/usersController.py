from flask import Flask, request
from flask_restplus import Namespace, Resource, Api, fields
import pymongo
from bson import ObjectId
from database import get_db
import hashlib

api = Namespace('users', description='User related operations')


locationPayload = api.model('locationPayload', {
    "provincia": fields.String,
    "canton": fields.String,
    "parroquia": fields.String
})

userPayload = api.model('userPayload', {
    "tipoUser" : fields.String(["admin","cliente","artesano"]),
    "tipoId" : fields.String,
    "identificacion": fields.String,
    "email" : fields.String,
    "apellidos": fields.String,
    "nombres": fields.String,
    "direccion": fields.String,
    "ubicacion": fields.Nested(locationPayload),
    "telefonos" : fields.List(fields.String),
    "password" : fields.String, #el password se almacena hasheado como MD5
    "estado": fields.Boolean, #activo 1, inactivo 0
    "intentos": fields.Integer, #numero de intentos para el login, max 3
    "servicios" : fields.List(fields.String) #solo si es artesano
})

userUpdatePayload = api.model('userUpdatePayload', {
    "tipoUser": fields.String(["admin", "cliente", "artesano"]),
    "tipoId": fields.String,
    "identificacion": fields.String,
    "email": fields.String,
    "apellidos": fields.String,
    "nombres": fields.String,
    "direccion": fields.String,
    "ubicacion": fields.Nested(locationPayload),
    "telefonos": fields.List(fields.String),
    "estado" : fields.Boolean,
    "intentos": fields.Integer,
    "servicios": fields.List(fields.String)
})

queryUsers = {"tipoUser": 1,
              "tipoId": 1,
              "identificacion": 1,
              "email": 1,
              "apellidos": 1,
              "nombres": 1,
              "direccion": 1,
              "ubicacion": 1,
              "telefonos": 1,
              "estado": 1,
              "intentos": 1,
              "servicios": 1
              }

userParser = api.parser()
userParser.add_argument(
    'page', type=int, help='page number', location='head')
userParser.add_argument('pageSize', type=int,
                          help='page size', location='head')


@api.route('/')
class People(Resource):
    @api.doc(parser=userParser)
    def get(self):
        db = get_db()
        args = request.args
        page = int(args['page'])
        pageSize = int(args['pageSize'])
        people = list(db["users"].find({}, queryUsers).skip(
            page * pageSize).limit(pageSize))
        for person in people:
            person['_id'] = str(person['_id'])
        return {"total": db['users'].count_documents({}), "items": people}, 200

    @api.expect(userPayload)
    def post(self):
        db = get_db()
        body = api.payload
        body['password'] = str(hashlib.sha256(body['password'].encode()).hexdigest())
        if db["users"].find_one({"tipoId": body["tipoId"], "identificacion": body["identificacion"]}) or db["users"].find_one({"email": body["email"]}):
            return {"personExists": True}, 400
        res = db["users"].insert_one(body)
        return {"_id": str(res.inserted_id)}, 200


@api.route('/<string:id>')
class Person(Resource):
    def get(self, id):
        db = get_db()
        res = db["users"].find_one({"_id": ObjectId(id)}, queryUsers)
        if res is None:
            return {"id": id}, 404
        res['_id'] = str(res['_id'])
        return res, 200

    def delete(self, id):
        db = get_db()
        res = db['users'].delete_one({"_id": ObjectId(id)})
        if res.deleted_count <= 0:
            return {"_id": id}, 404
        return {}, 200

    @api.expect(userPayload)
    def put(self, id):
        db = get_db()
        body = api.payload
        person = db['users'].find_one({"_id": ObjectId(id)})
        if person == None:
            return {"id": id}, 404
        db['users'].update_one({"_id": ObjectId(id)}, {"$set" : body})
        person = db['users'].find_one({"_id": ObjectId(id)})
        person['_id'] = str(person['_id'])
        return person, 200
