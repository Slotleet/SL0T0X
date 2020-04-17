#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

import sqlite3
import io
import secrets

conn = sqlite3.connect('SQLite.db')
with io.open('backup/SQLite-' + secrets.token_hex(5) + '.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)
print('Backup performed successfully.')
print('Saved...')
conn.close()
