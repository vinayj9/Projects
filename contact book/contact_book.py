# contacts={'john smith':{'phone':100,'email':'abc@email'},
#           'erin doe':{'phone':101,'email':'abc1@email'}}
contacts={}
print('Welcome to your contact book')

def view_contacts():
    if not contacts:
        print('No contacts found')
        return
    for x,y in contacts.items():
        # print(f'name:{x}{y}')
        print(f'name:{x}, phone:{y['phone']}, email:{y['email']}')

def add_contacts():
    name=input("Enter contact's name:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    if name in contacts:
        print('Contact already exists')
        a=input('Do you want to overwrite contact?(y/n)')
        if a=='y':
            contacts[name.strip()]={'phone':phone.strip(),'email':email.strip()}
            print('Contact overwrite successful!')
            return
        elif a=='n':
            return
        else:
            print('Invalid input!')
            return
    contacts[name.strip()]={'phone':phone.strip(),'email':email.strip()}
    print('Contact added successfully')

def search_contact():
    a=input('Search name:')
    # if a in contacts:
    #     print(contacts.get(a))
    # else:
    #     print('Contact not found!')
    for x in contacts:
        if x.lower()==a.lower():
            print(contacts.get(x))
            break
    else:
        print('Contact not found!')

def delete_contact():
    a=input('Specify name:')
    for x in contacts:
        if a.lower()==x.lower():
            print(contacts.get(x))
            b=input('Want to delete contact?(y/n):')
            if b=='y':
                contacts.pop(x)
                print('Contact deleted')
                break
            else:
                return
    else:
        print('Contact not found!')

def show_menu():
    print('1.Add Contact\n2.View All Contacts\n3.Search Contact\n4.Delete Contact\n5.Exit ')
    return

while True:
    print()
    show_menu()
    a=input('Select your choice of action(1/2/3/4/5):')
    if a=='1':
        add_contacts()
    elif a=='2':
        view_contacts()
    elif a=='3':
        search_contact()
    elif a=='4':
        delete_contact()
    elif a=='5':
        print('Goodbye!')
        break
    else:
        print('Invalid input!')
        continue
        
        
        






