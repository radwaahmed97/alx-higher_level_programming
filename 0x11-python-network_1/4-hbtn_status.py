#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    txt = req.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
