import json

def get_data():
    d={}
    with open('config.json') as f:
        d = json.load(f)
        f.close()
    return d
