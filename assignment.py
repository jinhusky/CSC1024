"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime as datetime_s

def main():
    # prints user interface menu
    database = []
    with open("books.txt") as txtfile:

            for line in txtfile:
                ISBN, author, title, publisher, genre, year_published, date_purchased, status = line.rstrip().split(",")
                book = {"ISBN": ISBN, "author": author, "title": title, "publisher": publisher
                            , "genre": genre, "year_published": year_published, "date_purchased": date_purchased, "status": status}
                database.append(book)

     
    prg_end = False 
    show_menu()

    #run program until user selects exit option
    while prg_end == False:
        try:
            option = input("\nSelect option (1 to 6): ")

            if int(option) == 1:
                add_book(database)
            
            elif int(option) == 2:
                ...

            elif int(option) == 6:
                prg_end = True

            elif option == "":
                continue
            
        
        except ValueError:
            print("Invalid input please enter 1 to 6")
            continue

    print(database)

    with open("new_books.txt", "w") as new_file:
        for book in database:
            try:
                book_info = ','.join([book['ISBN'], book['author'], book['title'], book['publisher'],
                            book['genre'], book['year_published'], book['date_purchased'], book['status']])
                
            except TypeError:
                pass

            new_file.write(book_info + "\n")
            

"""
clear screen
    os.system(f"ipconfig /all") 
"""
    
def add_book(database):

    ISBN = get_ISBN("\nEnter International Standard Book Number (13-digits): ")      
    author = get_author("\nEnter author name: ")
    title = input("\nEnter title of book: ")
    publisher = get_alpha("\nEnter publisher name: ")
    genre = get_alpha("\nEnter book's genre: ")
    year_published = get_year_published("\nEnter the year book was published: ")
    date_purchased = get_date_purchased("\nEnter the date book was purchased (e.g. 13-08-2000): ")
    status = get_status("\nEnter the status of the book (e.g. 'read' or 'to-read')")
    book = {"ISBN": ISBN, "author": author, "title": title, "publisher": publisher
                            , "genre": genre, "year_published": year_published, "date_purchased": date_purchased, "status": status}
    database.append(book)
    print(database)

def get_ISBN(prompt):
    while True:
        ISBN = input(prompt)

        if len(ISBN) == 3 and ISBN.isdigit():
            return str(ISBN)
        else:
            print("Invalid input. Please enter a 13-digit number.")

def get_author(prompt):
    while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() or char == '.' for char in author):
            # Allow alphabets, spaces, and dots in the author name
            return str(author.title())
        else:
            print("Invalid input. Please enter a valid author name.")

def get_alpha(prompt):
     while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() for char in author):
            return str(author.title())
        else:
            print("Invalid input. Please enter a valid author name.")

def get_year_published(prompt):
    while True:
        try:
            number = int(input(prompt))
            if (number > 2023 or number < 1):
                continue
            
        except ValueError:
            print("Invalid input, please enter a valid number!")
            continue
    
        return str(number)

def get_date_purchased(prompt):
    while True:
        try:
            date_str = input(prompt)
            #convert the input string into datetime object with dd-mm-yyyy format
            date_obj = datetime_s.datetime.strptime(date_str, "%d-%m-%Y")

            return str(date_obj.strftime("%d-%m-%Y"))
        
        except ValueError:
            print("Invalid input. Please enter the date in the format (dd-mm-yyyy): ")

def get_status(prompt):
    while True:
        status = input(prompt)

        if status == "read" or status == "to-read":
            return str(status)
                 
        else:
            print("Invalid input. Please enter either \"read\" or \"to-read\".")
    


def show_menu():
    print(f"[1] Add Book Record(s)\n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n")
          

if __name__ == "__main__":
    main()