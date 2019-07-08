from textapp import create_app

from textapp.models import db
app = create_app()

if __name__ == '__main__':
    # db.create_all()
    app.run()