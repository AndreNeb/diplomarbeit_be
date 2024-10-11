import os
from flask import Flask

def create_app(test_config=None):   # create and configure app
    app = Flask(__name__, instance_relative_config=True)    # create flask instance; __name__ current Python module; tells app that configuration files are relative
                                                            # to instance folder; older is located in flaskr package
    app.config.from_mapping(    # default configuration that app will use
        SECRET_KEY='dev',   # to keep data safe; dev provides convenient value during development, but should be overridden with random value when deploying
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),  # path to database
    )

    if test_config is None: # load instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)    # overrides default configuration with values taken from config.py
    else:   # load test config if passed in
        app.config.from_mapping(test_config)    # loads config test_config

    try:    # ensure instance folder exists
        os.makedirs(app.instance_path)  # ensures app.instance_path exists
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello World'

    return app




