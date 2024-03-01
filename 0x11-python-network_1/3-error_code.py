#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
