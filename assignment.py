"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime

def main():
    show_menu()
    options_menu = get_int_menu("Select option: ")

    books = []

    with open("books.txt") as txtfile:
        for line in txtfile:
            ISBN, author, title, publisher, genre, year_published, date_purchased, status = line.rstrip().split(",")
            book = {"ISBN": ISBN, "author": author, "title": title, "publisher": publisher
                          , "genre": genre, "year_published": year_published, "date_purchased": date_purchased, "status": status}
            books.append(book)
            
    print(books)

    




"""
clear screen
    os.system(f"ipconfig /all") 
"""
    
def add_book(database):
    ...
    


def get_int_menu(num):
    while True:
        try:
            option = int(input(num))
            if option < 1 or option > 6: 
                print("Invalid input please enter 1 to 6")
                continue
        
        except ValueError:
            print("Invalid input, please enter a number!")
            continue
    
        return option

def show_menu():
    print(f"[1] Add Book Record(s)\n[2] Update/Edit Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit")
          

if __name__ == "__main__":
    main()