


from .text import Text


def init_set(version,app):
    vesis = {
        "text":Text()
    }
    vesis[version].to_set(app=app)