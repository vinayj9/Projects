import modules.data as data
def isvalid_phone(phone):
    while not phone.isdigit():
        print('Invalid contact')
        phone=input("Enter phone number:").strip()
    return phone

def isvalid_email(email):
    while True:
        at=email.find('@')
        dot=email.find('.', at+1)
        if at !=-1 and dot !=-1:
            return email
        print('Invalid email')
        email=input("Enter email:").strip()
    
    # while True:
    #     try:
    #         at = email.index('@')
    #         dot = email.index('.', at+1)  
    #         return email
    #     except ValueError:
    #         print('Invalid email')
    #         email = input("Enter email: ").strip()
    
    # while True:
    #     if '@' not in email or '.' not in email:
    #         print('Invalid email')
    #         email = input("Enter email: ").strip()
    #     else:
    #         return email

def isinvalid_name(name):
    while not name.replace(' ','').isalpha():
        print('Invalid name')
        name=input("Enter contact's name:").strip()
    return name
   
def add_contacts():
    name=input("Enter contact's name:").strip()
    phone=input("Enter phone number:").strip()
    email=input("Enter email:").strip()
    if name in data.contacts:
        print('Contact already exists')
        a=input('Do you want to overwrite contact?(y/n)')
        if a=='y':
            name=isinvalid_name(name)
            phone=isvalid_phone(phone)
            email=isvalid_email(email)
            data.contacts[name]={'phone':phone,'email':email}
            print(f"Contact '{name}' overwrite successful!")
            return
        elif a=='n':
            return
        else:
            print('Invalid input!')
            return
    name=isinvalid_name(name)
    phone=isvalid_phone(phone)
    email=isvalid_email(email)
    data.contacts[name]={'phone':phone,'email':email}
    print(f"Contact '{name}' added successfully")
