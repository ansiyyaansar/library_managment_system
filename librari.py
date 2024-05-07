Library=[]
def add_book():
    idnum=int(input("enter id : "))
    name=input("enter your name : ")
    author=input("enter author name: ")

    bookdetails ={
        "idno":idnum,
        "name":name,
        "author":author
    }
    Library.append(bookdetails)
    print(f"{idnum}id number added successfully")

def display_book():
    displayid=int(input("enter your display id :"))
    for book in Library:
        if book["idno"]==displayid:
            
            print(book)


def search_book():
    searchid=int(input("enter id number to search:"))
    for book in Library:
        if book["idno"]==searchid:
            print("data fetch succesfully")
            print(f"id : {book['idno']} , {book['name']} , {book['author']} ")
        
        else:
            print("invalid id")


def delete_book():
    deleteid=int(input("enter id number to delete: "))
    for book in Library:
        if book['idno']==deleteid:
            Library.remove(book)
            print("delete")
        else:
            print("invalid id") 


while True:
    print("----\noption----------")
    print("----1 ADD books----")
    print("----2 display books---")
    print("----3 SEARCH book----")
    print("----4 delete----")
    print("----5 exit-----")
    choice=int(input("enter choice: "))

    if choice == 1:
        add_book()
    elif choice==2:
        display_book()
    elif choice==3:
        search_book()
    elif choice==4:
        delete_book()
    elif choice==5:
        break
    else:
        print("enter a valid input")