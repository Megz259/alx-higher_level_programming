#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response
"""


import sys
import urllib.error
import urllib.request


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
