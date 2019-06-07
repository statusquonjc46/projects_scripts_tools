#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class SendEmail(FlaskForm):
    alias = StringField('Alias', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=10)])
    body = StringField('Body', validators=[DataRequired(), Length(min=2, max=140)])


class EditorLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
