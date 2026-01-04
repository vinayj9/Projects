import modules.data as data

def search_contact():
    a=input('Search name:')
    count=1
    # for name in contacts:
    #     if a.lower() in name.lower():
    #         print(f'{count}.{contacts[name]}')
    #         break
    # if a in contacts:
    #     print(contacts.get(a))
    # else:
    #     print('Contact not found!')
    for x,y in data.contacts.items():
        # if x.lower()==a.lower():
        #     print(contacts.get(x))
        if a.lower() in x.lower():
            print(f'{count}.name:{x}, phone:{y['phone']}, email:{y['email']}')
            count+=1
    if count==1:
        print('Contact not found!')

