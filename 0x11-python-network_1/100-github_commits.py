#!/usr/bin/python3
"""
list 10 commits (from most recent to oldest)
takes 2 arguments in order to solve this challenge.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    comms = r.json()
    for comm in comms[:10]:
        print(comm.get('sha'), end=': ')
        print(comm.get('commit').get('author').get('name'))
