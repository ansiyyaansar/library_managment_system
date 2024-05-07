import os
import json
Library={'count':0,'library list':[]}

def clear():
    os.system("clear")

def save_file():
    with open('grocerymangment.json','w+')as file:
        json.dump(Library,file,indent=4)
        print("added succesfully")

def add_book():
    clear()
    flag=0
    while flag==0:
        try:
            idnum=int(input("enter id : "))
            name=input("enter your name : ")
            author=input("enter author name: ")
            break
        except:
            print("invalid character")

    bookdetails ={
        "idno":idnum,
        "name":name,
        "author":author
    }
    Library["count"]+=1
    Library["library list"].append(bookdetails)
    print(f"{idnum}id number added successfully")

def display_book():
    clear()
    flag=0
    try:
        displayid=int(input("enter your display id :"))
        for book in Library["library list"]:
            if book["idno"]==displayid:
                print(book)
                flag=1
                break
            if flag == 0:
                print("item not exists")
    except:
        print("invalid character")


def search_book():
    clear()
    flag=0
    try:
        searchid=int(input("enter id number to search:"))
        for book in Library["library list"]:
            if book["idno"]==searchid:
                print("data fetch succesfully")
                print(f"id : {book['idno']} , {book['name']} , {book['author']} ")
                flag=1
                break
            if flag ==0:
                print("item not exists")
    except:
        print("invalid id")


def delete_book():
    clear()
    flag=0
    try:
        deleteid=int(input("enter id number to delete: "))
        for book in Library["library list"]:
            if book['idno']==deleteid:
                Library["library list"].remove(book)
                Library['count']-=1
                print("delete")
                flag=1
                save_file()
                break
            if flag == 0:
                print("item not exist")
    except:
        print("invalid id") 

def main():
    clear()
while True:
    try:
        print("----\noption----------")
        print("----1 ADD books----")
        print("----2 display books---")
        print("----3 SEARCH book----")
        print("----4 save_file----")
        print("----5 delete----")
        print("----6 exit-----")
        choice=int(input("enter choice: "))

        if choice == 1:
            add_book()
        elif choice==2:
            display_book()
        elif choice==3:
            search_book()
        elif choice==4:
            save_file()
        elif choice==5:
            delete_book()
        elif choice==5:
            break
        else:
            print("enter a valid input")
    except:
        print("invalid character")
if __name__=='__main__':
    main()

