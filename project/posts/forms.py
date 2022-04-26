from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=6, max=250)])

    content = TextAreaField('Content')

    submit = SubmitField('Submit post')
    link = StringField('Link')
    image = StringField('Image link')
    featured = BooleanField('Is Featured')
