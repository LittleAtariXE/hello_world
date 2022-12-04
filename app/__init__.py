from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # route code
    from .main import main_blueprint
    from .notepad import notepad_blueprint
    from .make_fake import make_fake_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(notepad_blueprint, url_prefix='/notepad')
    app.register_blueprint(make_fake_blueprint, url_prefix='/make_fake')

    return app


