import modules.data as data

def view_contacts():
    if not data.contacts:
        print('No contacts found')
        return
    for i,(x,y) in enumerate(sorted(data.contacts.items()), start=1):
        # print(f'name:{x}{y}')
        print(f'{i}.name:{x}, phone:{y['phone']}, email:{y['email']}')