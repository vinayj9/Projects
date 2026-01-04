import modules.data as data
def delete_contact():
    a=input('Specify name:')
    for x in data.contacts:
        if a.lower()==x.lower():
            print(data.contacts.get(x))
            b=input('Want to delete contact?(y/n):')
            if b=='y':
                data.contacts.pop(x)
                print(f"Contact '{a}' deleted")
                break
            else:
                return
    else:
        print('Contact not found!')