#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

import pytz
from datetime import datetime
from flask_login import UserMixin
from SL0T0X import db, login_manager, app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, server_default=str('admin'))
    password = db.Column(db.String(60), unique=True, nullable=False,
                         server_default=str('$2b$12$Xqi8WVW.kq7DiQfwQoZ4euXmWG6ankR/3pjD9YqfFRFAjNcQeb0d6'))

    def __repr__(self):
        return f"User('{self.id}', '{self.username}')"


class Pentest(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(300), nullable=False)
    ipaddress = db.Column(db.String(20), nullable=False, default='No Entry')
    server = db.Column(db.String(90), nullable=False, default='No Entry')
    type = db.Column(db.String(90), nullable=False, default='No Entry')
    script = db.Column(db.String(90), nullable=False, default='No Entry')
    vulns = db.Column(db.Text(), nullable=False, default='No Entry')
    nmap = db.Column(db.Text(), default='nmap.txt')
    godirb = db.Column(db.Text(), default='dirb.txt')
    notes = db.Column(db.Text(), nullable=False, default='No Entry')
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone(app.config['TimeZone'])))
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Pentest('{self.id}', '{self.url}', '{self.ipaddress}'," \
               f"'{self.server}', '{self.type}', '{self.script}', '{self.nmap}'," \
               f"'{self.godirb}', '{self.notes}', '{self.date}', '{self.status}')"


class Note(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(160), nullable=False)
    note = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone(app.config['TimeZone'])))

    def __repr__(self):
        return f"Notes('{self.id}', '{self.name}', '{self.note}', '{self.date}')"


class Persons(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(90), nullable=False)
    pnumber = db.Column(db.String(90), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    accounts = db.Column(db.String(300), nullable=False)
    note = db.Column(db.Text())
    avatar = db.Column(db.Text())
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone(app.config['TimeZone'])))

    def __repr__(self):
        return f"SE('{self.id}', '{self.name}', '{self.birthday}'," \
               f"'{self.email}', '{self.pnumber}', '{self.locaiton}', '{self.accounts}'," \
               f"'{self.note}', '{self.avatar}')"
