def register_bp(app):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


def register_db(app):
    pass



def register_ss(app):
    pass



def create_app():
    from flask import Flask
    app = Flask(__name__)
    register_bp(app)
    return app


