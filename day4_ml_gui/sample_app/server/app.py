from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    return app


app = create_app('config.Config')
CORS(app)

from model import db
db.init_app(app)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Routes
# from resources.hello import HelloResource
# from resources.category import CategoryResource
# from resources.comment import CommentResource
from resources.entry import EntryResource
from resources.passenger import PassengerResource

# api.add_resource(HelloResource, '/hello')
# api.add_resource(CategoryResource, '/category')
api.add_resource(EntryResource, '/entry')
api.add_resource(PassengerResource, '/passenger')


app.register_blueprint(api_bp, url_prefix='/api')
