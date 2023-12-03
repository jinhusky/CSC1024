"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime

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
    
        option = input("Select option (1 to 6): ")

        if int(option) == 1:
            add_book(database)
        
        elif int(option) == 2:
            ...

        elif int(option) == 6:
            prg_end = True

        elif option == "":
            continue
        
        else:
            print("Invalid input please enter 1 to 6")
            continue

    print(database)
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
    book = {"ISBN": ISBN, "author": author, "title": title, "publisher": publisher
                            , "genre": genre, "year_published": year_published, "date_purchased": date_purchased, }
    database.append(book)

    print(ISBN, author, title, publisher, genre, year_published, date_purchased)

def get_ISBN(prompt):
    while True:
        ISBN = input(prompt)

        if len(ISBN) == 3 and ISBN.isdigit():
            return ISBN
        else:
            print("Invalid input. Please enter a 13-digit number.")

def get_author(prompt):
    while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() or char == '.' for char in author):
            # Allow alphabets, spaces, and dots in the author name
            return author.title()
        else:
            print("Invalid input. Please enter a valid author name.")

def get_alpha(prompt):
     while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() for char in author):
            return author.title()
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
    
        return number

def get_date_purchased(prompt):
    ...


def show_menu():
    print(f"[1] Add Book Record(s)\n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n")
          

if __name__ == "__main__":
    main()