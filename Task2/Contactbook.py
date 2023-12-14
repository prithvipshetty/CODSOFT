contact={}


def display_contact():
    print("Name\t\tContact number\t\tEmail\t\tAddress")
    for key in contact:
        name,phone,email,address=contact[key]
        print("{}\t\t{}\t\t{}\t\t{}".format(name,phone,email,address))


while True:
    choice=int(input(" 1.Add \n 2.Search \n 3.View \n 4.Update \n 5.Delete \n 6.Exit\n Enter your choice:"))
    if choice==1:
        name=input("Enter the contact name:")
        phone=input("Enter the mobile number:")
        email=input("Enter the email:")
        address=input("Enter the address:")
        contact[name]=(name,phone,email,address)
    elif choice==2:
        search_name=input("Enter the contact name:")
        if search_name in contact:
            name,phone,email,address=contact[search_name]
            print("{}'s contact number is {}, email is {}, and address is {}".format(name,phone,email,address))
        else:
            print("Name is not found in contact book")
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the contact to be updated:")
        if edit_contact in contact:
            phone=input("Enter mobile number:")
            email=input("Enter email:")
            address=input("Enter address:")
            contact[edit_contact]=(edit_contact,phone,email,address)
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in the contact book")
    elif choice==5:
        del_contact=input("Enter the contact to be deleted:")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact (y/n)?")
            if confirm.lower()=='y':
                contact.pop(del_contact)
                display_contact()
        else:
            print("Name is not found in the contact book")
    else:
        break
