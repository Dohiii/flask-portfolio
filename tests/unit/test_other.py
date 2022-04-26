from slugify import slugify


def test_slugify():
    txt = "This is a test ---"
    slug = slugify(txt)
    assert slug == "this-is-a-test"
