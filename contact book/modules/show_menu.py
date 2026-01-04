from modules.data import contacts
def show_menu():
    x=len(contacts)
    if x==1:
        print(f'{x} Contact')
    elif x==0:
        None
    else:
        print(f'{x} Contacts')
    print('1.Add Contact\n2.View All Contacts\n3.Search Contact\n4.Delete Contact\n5.Exit ')
    return