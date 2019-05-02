from flask import Flask
from app import app
# def create_app(config_filename):
#     app = Flask(__name__)
#     print('config_filename:', config_filename)
#     app.config.from_object(config_filename)
    
#     from model import db
#     db.init_app(app)

#     from app import api_bp
#     app.register_blueprint(api_bp, url_prefix='/api')

#     return app


if __name__ == "__main__":
    # app = create_app('config')
    # app = create_app('config.Config')
    # app.run(debug=True)
    app.run(host='0.0.0.0')
