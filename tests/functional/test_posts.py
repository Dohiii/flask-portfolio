"""
This file (test_recipes.py) contains the functional tests for the `recipes` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `recipes` blueprint.
"""
from project import create_app
from project.models import Post


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"O mnie" in response.data


def test_post_page(test_client, init_database):
    response = test_client.get("/posts")
    assert response.status_code == 200
    assert b"<h3>Projecty</h3>" in response.data
    assert b"https://github.com/" in response.data


def test_single_post_page(test_client, init_database):
    response = test_client.get("/post-title")
    assert response.status_code == 200
    assert b"Post Title" in response.data
    assert b"https://image.com/" in response.data


def test_edit_post_page(test_client, init_database):
    response = test_client.get("/edit/post-title")
    assert response.status_code == 200
    assert b"Post Title" in response.data
    assert b"https://image.com/" in response.data


def test_add_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid NOT valid for add-post
    """
    flask_app = create_app('flask_test.cfg')
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/add-post')
        assert not response.status_code == 200
