#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

from SL0T0X import app
from SL0T0X.utils import header
from sys import exit, version_info


def main():
    if version_info < (3, 0, 0):
        print('[!] Please use Python 3. $ python3 SocialFish.py')
        exit(0)
    header()
    app.run(host="0.0.0.0", port=1337)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
