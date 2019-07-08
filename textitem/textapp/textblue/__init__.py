from .tblue import tblue


def init_blue(app):
    app.register_blueprint(tblue)