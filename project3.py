
Contact={}

def ShowFunction():
   print (Contact.items())
   print("Name \t Contact")
   for key in Contact:
      print("{} \t {}".format(key, Contact.get(key)))
while True:
    choice= int(input("1.Add your Contact \n"
        "2.Search your Contact \n"
        "3.Display your Contact \n"
        "4.Edit your Contact \n"
        "5.Delete Contact \n"
        "6.Exit \n"
        "Please Write Number of Between 1-6 : "))
   
    if choice ==1 :
     Name=input("Add Your Contact Name: ")
     Phone=input("Enter your Phone number:")
     Contact[Phone]= Name


    elif choice ==2 :
     ContactName= input("Search the Contact Name: ")
     if ContactName in Contact:
       print(ContactName, "Contact Name is ",Contact[ContactName])
     else :
       print("not found the contact")

    elif choice ==3:
     if not Contact:
       print("Contact book is empty")
     else : 
       ShowFunction ()  
       
    elif choice ==4:
     EditContact= input("Edit Contact:")
     
     if EditContact in Contact:
       phone = input("Change the contact")
       Contact[EditContact] = phone
       print("Contact upload successful ")
       ShowFunction ()
     else:
      print("Name is Not Found")

    elif choice ==5:
     DeleteContact = input("which Contact Do you want to Delete")
     if DeleteContact in Contact:
        DeletedConfirm = input (" do you want to delete this contact y/n")
        if DeletedConfirm =="y" or DeletedConfirm =="y":
         Contact.pop(DeleteContact)
         ShowFunction()
     else : 
      print("the contact can not be found in")
    else :
      break

      