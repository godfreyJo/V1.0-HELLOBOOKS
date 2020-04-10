from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired




class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])   
    bookPicture = FileField('Book Picture', validators=[FileAllowed(['jpg', 'png'])]) 
    submit = SubmitField('Post')