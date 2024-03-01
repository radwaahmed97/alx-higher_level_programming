#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = requests.get("https://api.github.com/user", authen=authen)
    print(resp.json().get("id"))
