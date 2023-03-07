from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField, SubmitField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
  id = IntegerField('id', validators=[DataRequired()])
  title    = StringField('title', validators=[DataRequired()])
  author    = StringField('author', validators=[DataRequired()])
  country    = StringField('country', validators=[DataRequired()])
  imageLink    = StringField('imageLink', validators=[DataRequired()])
  language    = StringField('language', validators=[DataRequired()])
  pages    = IntegerField('pages', validators=[DataRequired()])
  year    = IntegerField('year', validators=[DataRequired()])
  link    = StringField('link', validators=[DataRequired()])
  method = HiddenField('PUT')
  button = SubmitField('update')

class CreateNew(FlaskForm):
  title    = StringField('title', validators=[DataRequired()])
  author    = StringField('author', validators=[DataRequired()])
  country    = StringField('country', validators=[DataRequired()])
  imageLink    = StringField('imageLink', validators=[DataRequired()])
  language    = StringField('language', validators=[DataRequired()])
  pages    = IntegerField('pages', validators=[DataRequired()])
  year    = IntegerField('year', validators=[DataRequired()])
  link    = StringField('link', validators=[DataRequired()])
  method = HiddenField('POST')
  button = SubmitField('create')

class DeleteForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    method = HiddenField('DELETE')
    button = SubmitField('delete')

class GetBookByID(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    method = HiddenField('GET')
    button = SubmitField('search')