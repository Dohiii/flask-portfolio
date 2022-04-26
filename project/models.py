
from project import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * email - email address of the user
        * hashed password - hashed password (using werkzeug.security)
        * registered_on - date & time that the user registered

    REMEMBER: Never store the plaintext password in a database!
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hashed = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, email: str, password_plaintext: str):
        """Create a new User object using the email address and hashing the
        plaintext password using Werkzeug.Security.
        """
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)
        self.registered_on = datetime.now()

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)

    def set_password(self, password_plaintext: str):
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)

    def __repr__(self):
        return f'<User: {self.email}>'

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.Text)
    link = db.Column(db.String)
    image = db.Column(db.String)
    featured = db.Column(db.Boolean, default=False)
    created = db.Column(db.Date)
    slug = db.Column(db.String(140))

    def __init__(self, title: str, content: str, link: str, image: str, featured: bool, slug: str):
        self.title = title
        self.content = content
        self.link = link
        self.image = image
        self.featured = featured
        self.slug = slug
        self.created = datetime.now()
