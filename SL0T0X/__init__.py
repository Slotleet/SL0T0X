#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from SL0T0X import config


db = SQLAlchemy(app)
crypt = Bcrypt(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.session_protection = "strong"
SimpleMDE(app)

# !- [ Fixing circular import  ] -!

from SL0T0X import routes, formroutes
