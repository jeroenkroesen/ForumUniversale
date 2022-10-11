import os
from flask import Flask

# The flask script is given this package
# Then it autodetects app or application
# Or in this case: an application factory called create_app
# It also recognizes a factory called make_app automagically
def create_app():
    ## create and configure the app
    # Tell Flask to store config relative to the instance folder
    # By default, config files are relative to the app root
    app = Flask(__name__, instance_relative_config=True)

    # Load the instance config
    app.config.from_pyfile('config.py', silent=True)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Database setup with SQLAlchemy
    # SQLAlchemy needs access to current_app.config
    # So we need to manually push the app context
    with app.app_context():
        from .database import DbSession

    # Register closing the db on teardown
    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        DbSession.remove()


    # Pages module
    from .controllers import pages
    app.register_blueprint(pages.bp)
    # Make pages/homepage route the default route
    app.add_url_rule('/', endpoint='pages.homepage')

    # Users module
    from .controllers import users
    app.register_blueprint(users.bp)

    return app
