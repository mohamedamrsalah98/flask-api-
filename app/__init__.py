
from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import projectConfig as AppConfig
from app.models import Post, Categories
from flask_restful import Api
from app.posts.api.api_views import HelloWorld,PostList,PostOperation


def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config

    app.config.from_object(current_config)
    db.init_app(app)

    # ## add migration
    migrate = Migrate(app, db, render_as_batch=True)

    from app.category import Categ_blueprint
    from app.posts import posts_blueprint
    app.register_blueprint(Categ_blueprint)
    app.register_blueprint(posts_blueprint)

    ######### Api

    api = Api(app)

    api.add_resource(HelloWorld, '/api/hello')
    api.add_resource(PostList, '/api/posts')
    api.add_resource(PostOperation, '/api/posts/<int:id>')



    return app
