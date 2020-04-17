#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

from SL0T0X import app

'''

    [#] Configuration: 
        - Main config

'''

app.config['DEBUG'] = True
app.config['PERPAGE'] = 5
app.config['TimeZone'] = 'Asia/Beirut'
app.config['SECRET_KEY'] = '6eb44a4f113d7a7f0cc7f761c91f8080'
app.config['UPLOAD_FOLDER'] = './static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQLite.db'
app.config['SIMPLEMDE_JS_IIFE'] = True
app.config['SIMPLEMDE_USE_CDN'] = False
app.config['ALLOWED_EXTENSIONS'] = 'png', 'jpg', 'jpeg', 'gif'
