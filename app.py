import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import  Api
from resources.item import ItemList, Item
from resources.user import UserRegister
from resources.store import Store, StoreList
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "sqlite:///data.db" )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'sinna'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=9000, debug=True)
