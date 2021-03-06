import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) # __name__ - name of current Python package
    # default configuration app will use
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load the instance config
        app.config.from_pyfile("config.py", silent=True) #overrides configurations from default config file
    else:
        #load test config
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello World!"

    from . import db
    db.init_app(app)

    return app