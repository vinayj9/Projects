import json
import modules.data as data
def load_contacts():
    try:
        with open("contacts.json") as f:
            data.contacts=json.load(f)
    except FileNotFoundError or json.JSONDecodeError:
        data.contacts={}
    