#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == '__main__':
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
