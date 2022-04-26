from project import create_app, db
from flask_migrate import Migrate
from project.models import User, Post

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app('flask.cfg')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)
