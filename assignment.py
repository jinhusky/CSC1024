"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime as datetime_s

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    
def main():
    # prints user interface menu
    database = []
    index = 1
    keys = ["INDEX", "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
    
    try:
        with open("books.txt") as txtfile:
            try:
                for line in txtfile:
                    ISBN, author, title, publisher, genre, year_published, date_purchased, status = line.rstrip().split(",")
                    book = {"INDEX": str(index), "ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
                    database.append(book)
                    index += 1
            #to avoid bug where trying to split an empty line 
            except ValueError:
                pass

    except FileNotFoundError:
        print(color_font("File not found. Create books.txt or check the file path.", colors.RED))

    prg_end = False 

    #run program until user selects exit option
    while prg_end == False:
        
        clearScreen()
        show_options()
        try:

            option = input("\nSelect option (1 to 6): ")

            if int(option) == 1:
                add_book(database)
                print(color_font("Book was successfuly added", colors.GREEN))
            
            elif int(option) == 2:
                display_books(database, keys)
                delete_book(database)

            elif int(option) == 4:
                display_books(database, keys)
                input()

            elif int(option) == 5:
                search_books(database, keys)
                
            elif int(option) == 6:
                prg_end = True

            elif option == "":
                continue

            
        except ValueError:
            input(color_font("Invalid input please enter 1 to 6", colors.RED))
            continue

    print(database)

    with open("new_books.txt", "w") as new_file:
        for book in database:
            try:
                book_info = ','.join([book['ISBN'], book['Author'], book['Title'], book['Publisher'],
                            book['Genre'], book['Year Published'], book['Date Purchased'], book['Status']])
                
            except TypeError:
                pass

            new_file.write(book_info + "\n")
            


def clearScreen():
    return os.system("cls" if os.name == 'nt' else 'clear')
#Cat was here
def add_book(database):
    repeat = True
    while repeat:
        ISBN = get_ISBN("\nEnter International Standard Book Number (13-digits): ")      
        author = get_author("\nEnter author name: ")
        title = input("\nEnter title of book: ")
        publisher = get_alpha("\nEnter publisher name: ")
        genre = get_alpha("\nEnter book's genre: ")
        year_published = get_year_published("\nEnter the year book was published: ")
        date_purchased = get_date_purchased("\nEnter the date book was purchased (e.g. 13-08-2000): ", year_published)
        status = get_status("\nEnter the status of the book (e.g. 'read' or 'to-read'): ")
        book = {"ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
        database.append(book)
        repeat = cont_verify(input(color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))


def delete_book(database):
        delete_list = []
        delete_options = print(color_font(f"[1] Enter ISBN to delete \n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n", colors.BLUE))
        choice = input("\nEnter the index of book you wish to delete: ")
        for book in database:
            if book["INDEX"] == choice:
                delete_list.append(book)
        for book in delete_list:
            database.remove(book)
        print(color_font("Book(s) deleted successfully.", colors.GREEN))
        input()


def search_books(database, keys):
    repeat = True
    
    while repeat:
        found_book = []
        clearScreen()
        print(color_font(f"[1] General Search\n[2] Search by ISBN\n[3] Search by author\n[4] Search by title \n", colors.YELLOW))
        try:
            option = input("Enter your option here: ")

            if int(option) == 1:
                i = 0
                m = get_ISBN("\nEnter International Standard Book Number (13-digits): ")
                for book in database:
                    if book[keys[1]] == m:
                        found_book.append(book)
                        clearScreen()
                        display_books(found_book, keys)
                        i += 1
                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
                
            elif int(option) == 2:
                m = get_ISBN("\nEnter International Standard Book Number (13-digits): ")
                for book in database:
                    if book[keys[1]] == m:
                        found_book.append(book)
                        clearScreen()
                        display_books(found_book, keys)
                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
                    
            elif int(option) == 3:
                a = get_author("\nEnter author name: ")
                for book in database:
                    if book[keys[2]] == a:
                        found_book.append(book)
                        clearScreen()
                        display_books(found_book, keys)
                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))  
            
            elif int(option) == 4:
                ...
            else:
                input(color_font("Invalid input please enter 1 to 6", colors.RED))
                continue


            repeat = cont_verify(input(color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter 1 to 4", colors.RED))
            continue

def get_result()

def get_ISBN(prompt):
    while True:
        ISBN = input(prompt)

        if len(ISBN) == 13 and ISBN.isdigit():
            return str(ISBN)
        else:
            print(color_font("Invalid input. Please enter a 13-digit number.", colors.RED))

def get_author(prompt):
    while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() or char == '.' for char in author):
            # Allow alphabets, spaces, and dots in the author name
            return str(author.title())
        else:
            print(color_font(f"Invalid input. Please enter only alpha \".\" for author's name.", colors.RED))

def get_alpha(prompt):
     while True:
        author = input(prompt)

        if all(char.isalpha() or char.isspace() for char in author):
            return str(author.title())
        else:
            print(color_font(f"Invalid input. Please enter only alphabets.", colors.RED))

def get_year_published(prompt):
    while True:
        try:
            year = int(input(prompt))
            current_year = datetime_s.datetime.now().year
            if (year < 1 or year > current_year):
                print(color_font( "Published year cannot be in the future or B.C." , colors.RED))
                continue

        except (ValueError, TypeError):
            print(color_font(f"Invalid input, only enter digits for year", colors.RED))
            continue
    
        return str(year)

def get_date_purchased(prompt, year_published):
    while True:
        try:
            date_str = input(prompt)
            #convert the input string into datetime object with dd-mm-yyyy format
            date_obj = datetime_s.datetime.strptime(date_str, "%d-%m-%Y")
            if date_obj > datetime_s.datetime.now() or date_obj.year < int(year_published):
                print(color_font(f"Invalid input. Cant purchase books in the future (dd-mm-yyyy): ", colors.RED))
                continue

            return str(date_obj.strftime("%d-%m-%Y"))
        
        except ValueError:
            print(color_font(f"Invalid input. Please enter the date in the format (dd-mm-yyyy): ", colors.RED))

def get_status(prompt):
    while True:
        status = input(prompt)

        if status == "read" or status == "to-read":
            return str(status)
                 
        else:
            print(color_font("Invalid input. Please enter either \"read\" or \"to-read\".", colors.RED))
    
        """
    # Displaying book details
    for book in database:
        print(f"{book['ISBN']:<20}{book['author']:<20}{book['title']:<40}{book['publisher']:<20}"
              f"{book['genre']:<20}{book['year_published']:<20}")
    """
def display_books(database, keys):
    width = [9, 17, 10, 9, 13, 9, 18, 18, 10]
    for book in database: 
        for key in keys:
            if width[keys.index(key)] < len(book[key]):
                width[keys.index(key)] = len(book[key])        
    
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))

    index = 0
    print(color_font(f"|", colors.GREEN), end="")

    for i in keys:
        print("{:^{w}}{}".format(i, colors.GREEN +"|"+colors.ENDC, w=width[index]), end="")
        index += 1

    print()
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))

    i = 0
    for book in database: 
        print(color_font(f"|", colors.GREEN), end="")
        for i in range(len(keys)):
            print("{:^{w}}{}".format(book[keys[i]], colors.GREEN +"|"+colors.ENDC, w=width[i]),end="")
        print()
        i += 1
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))
    



def cont_verify(c):
     while True:
        answer = c.lower()

        if  answer == "no" or answer == "n":
            return False
        elif answer == "yes" or answer == "y":
            return True
        else:
            print(color_font("Invalid input. Please enter either \"no\" or \"yes\".", colors.RED))
    

def show_options():
    print(color_font(f"[1] Add Book Record(s)\n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n", colors.BLUE))

def color_font(text, color):
    return color+text+colors.ENDC

if __name__ == "__main__":
    main()
