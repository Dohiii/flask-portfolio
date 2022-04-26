"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from project.models import User, Post



def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.password_hashed != 'FlaskIsAwesome'
    assert user.__repr__() == '<User: patkennedy79@gmail.com>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_post():
    """
   GIVEN a Post model
   WHEN a new Post is created
   THEN check the title and content fields are defined correctly
   """
    post = Post('First Post', 'Content of first post it is a lot of content',
                'https:link.com', 'https://pictute.com', False, slug='first-post')
    assert post.title == 'First Post'
    assert post.content == 'Content of first post it is a lot of content'
    assert post.link == 'https:link.com'
    assert post.image == 'https://pictute.com'
    assert post.featured == False


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password_hashed != 'FlaskIsAwesome'


def test_new_post_with_fixture(new_post):
    """
    GIVEN a Post model
    WHEN a new User is created
    """
    assert new_post.title == 'Post Title'
    assert new_post.content != 'Not a Content'
    assert new_post.featured == False


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.password_hashed != 'MyNewPassword'
    assert new_user.is_password_correct('MyNewPassword')
    assert not new_user.is_password_correct('MyNewPassword2')
    assert not new_user.is_password_correct('FlaskIsAwesome')


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'
