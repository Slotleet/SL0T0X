#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from markupsafe import Markup
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, IPAddress, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remmeber Me')
    submit = SubmitField('Login')


class AddPT(FlaskForm):
    url = StringField('URL',
                      validators=[DataRequired(),
                                  Length(min=2, max=30)])
    ipaddress = StringField('Ip Address',
                            validators=[IPAddress(ipv4=True), DataRequired(), Length(min=2, max=16)])
    server = StringField('Server',
                         validators=[DataRequired()])
    type = StringField('Type',
                       validators=[DataRequired()])
    script = StringField('Script(s)',
                         validators=[DataRequired()])
    vuln = StringField('Vulnerabilities',
                       validators=[DataRequired()])
    nmapoutput = FileField('Nmap output',
                           validators=[DataRequired(), FileAllowed(['txt'])])
    godirb = FileField('GoBuster,dirb Output',
                       validators=[DataRequired(), FileAllowed(['txt'])])
    note = TextAreaField('Note', validators=[DataRequired(), FileAllowed(['txt'])])
    status = BooleanField('Active')
    style = Markup('<span data-feather="plus"></span>')
    submit = SubmitField('Submit')


class AddNT(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=90)])
    note = TextAreaField('Note')
    submit = SubmitField('Add')


class EditNT(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=90)])
    note = TextAreaField('Note')
    submit = SubmitField('Add')


class AddSE(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    Birthday = StringField('Birthday', validators=[DataRequired()])
    emailaddress = StringField('Email Address')
    pnumber = StringField('Phone Number')
    location = StringField('Location')
    picture = FileField('Upload Picture',
                        validators=[DataRequired(), FileAllowed(['png', 'jpg', 'gif', 'jpeg'])])
    archive = FileField('Upload Files', render_kw={'multiple': True},
                        validators=[FileAllowed(['txt', 'png', 'jpg', 'jpeg', 'db'])])
    accounts = StringField('Accounts')
    note = TextAreaField('Note')
    submit = SubmitField('Add')


class Settings(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=2, max=10),
                                         EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Submit')
