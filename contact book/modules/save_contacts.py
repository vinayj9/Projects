import modules.data as data
import json
def save_contacts():
    with open("contacts.json","w") as f:
        json.dump(data.contacts,f)