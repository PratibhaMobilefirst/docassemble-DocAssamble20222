import requests

def createuser():
    r = requests.get('https://randomuser.me/api/')
    if r.status_code != 200:
        raise Exception("Could not obtain the time")
    return r.json()