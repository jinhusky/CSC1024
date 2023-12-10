"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime as datetime_s

class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"

keys = ["INDEX", "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]

def title_GG(n):
    match n:
        case 0:
            title_ = \
            '''   
  ____              _      __  __                                   
| __ )  ___   ___ | | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
|  _ \ / _ \ / _ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_) | (_) | (_) |   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
|____/ \___/ \___/|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                   |___/                   
            '''
        case 1:
            title_ = \
            '''
    _       _     _   ____              _      ____                        _  __ __  
   / \   __| | __| | | __ )  ___   ___ | | __ |  _ \ ___  ___ ___  _ __ __| |/ /_\ \ 
  / _ \ / _` |/ _` | |  _ \ / _ \ / _ \| |/ / | |_) / _ \/ __/ _ \| '__/ _` | / __| |
 / ___ \ (_| | (_| | | |_) | (_) | (_) |   <  |  _ <  __/ (_| (_) | | | (_| | \__ \ |
/_/   \_\__,_|\__,_| |____/ \___/ \___/|_|\_\ |_| \_\___|\___\___/|_|  \__,_| |___/ |
                                                                             \_\ /_/            
                                          
            '''
        case 2:
            title_ = \
            '''
 ____       _      _         ____              _      ____                        _    __ __  
|  _ \  ___| | ___| |_ ___  | __ )  ___   ___ | | __ |  _ \ ___  ___ ___  _ __ __| |  / /_\ \ 
| | | |/ _ \ |/ _ \ __/ _ \ |  _ \ / _ \ / _ \| |/ / | |_) / _ \/ __/ _ \| '__/ _` | | / __| |
| |_| |  __/ |  __/ ||  __/ | |_) | (_) | (_) |   <  |  _ <  __/ (_| (_) | | | (_| | | \__ \ |
|____/ \___|_|\___|\__\___| |____/ \___/ \___/|_|\_\ |_| \_\___|\___\___/|_|  \__,_| | |___/ |
                                                                                      \_\ /_/                                          
            '''
        case 3:
            title_ = \
            '''
 _   _           _       _          _______    _ _ _     ____              _      ____                        _    __ __  
| | | |_ __   __| | __ _| |_ ___   / / ____|__| (_) |_  | __ )  ___   ___ | | __ |  _ \ ___  ___ ___  _ __ __| |  / /_\ \ 
| | | | '_ \ / _` |/ _` | __/ _ \ / /|  _| / _` | | __| |  _ \ / _ \ / _ \| |/ / | |_) / _ \/ __/ _ \| '__/ _` | | / __| |
| |_| | |_) | (_| | (_| | ||  __// / | |__| (_| | | |_  | |_) | (_) | (_) |   <  |  _ <  __/ (_| (_) | | | (_| | | \__ \ |
 \___/| .__/ \__,_|\__,_|\__\___/_/  |_____\__,_|_|\__| |____/ \___/ \___/|_|\_\ |_| \_\___|\___\___/|_|  \__,_| | |___/ |
      |_|                                                                                                         \_\ /_/ 
                                        
            '''
        case 4:
            title_ = \
            '''
  ____  _           _             _               ____              _    
|  _ \(_)___ _ __ | | __ _ _   _(_)_ __   __ _  | __ )  ___   ___ | | __
| | | | / __| '_ \| |/ _` | | | | | '_ \ / _` | |  _ \ / _ \ / _ \| |/ /
| |_| | \__ \ |_) | | (_| | |_| | | | | | (_| | | |_) | (_) | (_) |   < 
|____/|_|___/ .__/|_|\__,_|\__, |_|_| |_|\__, | |____/ \___/ \___/|_|\_\\n
            |_|            |___/         |___/                          

            '''
        case 5:
            title_ = \
            '''
 ____                      _     _               ____              _    
/ ___|  ___  __ _ _ __ ___| |__ (_)_ __   __ _  | __ )  ___   ___ | | __
\___ \ / _ \/ _` | '__/ __| '_ \| | '_ \ / _` | |  _ \ / _ \ / _ \| |/ /
 ___) |  __/ (_| | | | (__| | | | | | | | (_| | | |_) | (_) | (_) |   < 
|____/ \___|\__,_|_|  \___|_| |_|_|_| |_|\__, | |____/ \___/ \___/|_|\_\
                                         |___/                          
                                        
            '''
        case 6:
            title_ = \
            '''
 _____      _ _     ____                               __       _ _       
| ____|_  _(_) |_  / ___| _   _  ___ ___ ___  ___ ___ / _|_   _| | |_   _ 
|  _| \ \/ / | __| \___ \| | | |/ __/ __/ _ \/ __/ __| |_| | | | | | | | |
| |___ >  <| | |_   ___) | |_| | (_| (_|  __/\__ \__ \  _| |_| | | | |_| |
|_____/_/\_\_|\__| |____/ \__,_|\___\___\___||___/___/_|  \__,_|_|_|\__, |
                                                                    |___/ 
                                        
            '''
    print(title_)
    


def main():
    # prints user interface menu
    database = []
    index = 1
    
    try:
        with open("books_18058073.txt") as txtfile:
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

            option = input(color_font("\nSelect option (1-6): ", colors.YELLOW))

            if int(option) == 1:
                clearScreen()
                title_GG(1)
                add_book(database)
                print(color_font("Book was successfuly added", colors.GREEN))
            
            elif int(option) == 2:
                delete_book(database, year_published)

            elif int(option) == 4:
                clearScreen()
                title_GG(4)
                display_books(database)
                input()

            elif int(option) == 5:
                clearScreen()
                search_books(database)
                
            elif int(option) == 6:
                prg_end = True
                

            elif option == "":
                continue

        except ValueError:
            input(color_font("Invalid input please enter 1 to 6", colors.RED))
            continue

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
        status = get_status("\nEnter the status of the book (e.g. 'read' or 'to-read' or 'reading'): ")
        book = {"ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
        database.append(book)
        repeat = cont_verify(input(color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))


def delete_book(database, year_published):
    repeat = True
    
    while repeat:
        clearScreen()
        title_GG(2)
        display_books(database)
        print(color_font(
            "[1] Enter Index of book to delete\n"
            "[2] Enter ISBN of book to delete\n"
            "[3] Enter author of book to delete\n"
            "[4] Enter Title of book to delete\n"
            "[5] Enter Publisher of book to delete\n"
            "[6] Enter Genre of book to delete\n"
            "[7] Enter Year Published of book to delete\n"
            "[8] Enter Date Purchased of book to delete\n"
            "[9] Enter Status of book to delete\n"
            , colors.BLUE))
        
        try:
            option = input(color_font("\nSelect option (1-9): ", colors.YELLOW))
            
            if int(option) == 1:
                k = get_INDEX("\nPress Ctrl + d to back\nEnter INDEX of book to delete: ", database)
                found_book = []
                for book in database:
                    clearScreen()
                    if k == book[keys[0]]:
                        found_book.append(book)

                display_books(found_book)
                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
                
                
            
            elif int(option) == 2:
                found_list = searching_item(database, key = 1, k = get_ISBN("\nPress Ctrl + d to back\nEnter International Standard Book Number (13-digits) to delete: "))
                deleting_items(found_list, database)

            elif int(option) == 3:
                found_list = searching_item(database, key = 2, k = get_author("\nPress Ctrl + d to back\nEnter Author of book to delete: "))
                deleting_items(found_list, database)    

            elif int(option) == 4:
                found_list = searching_item(database, key = 3, k = input("\nPress Ctrl + d to back\nEnter Title of book to delete: "))
                deleting_items(found_list, database)

            elif int(option) == 5:
                found_list = searching_item(database, key = 4, k = get_alpha("\nPress Ctrl + d to back\nEnter Publisher of book to delete: "))
                deleting_items(found_list, database)

            elif int(option) == 6:
                found_list = searching_item(database, key = 5, k = get_alpha("\nPress Ctrl + d to back\nEnter Genre of book to delete: "))
                deleting_items(found_list, database)

            elif int(option) == 7:
                found_list = searching_item(database, key = 6, k = get_year_published("\nPress Ctrl + d to back\nEnter Year Published of book to delete: "))
                deleting_items(found_list, database)

            elif int(option) == 8:
                found_list = searching_item(database, key = 7, k = get_date_purchased("\nPress Ctrl + d to back\nEnter Date Purchased of book to delete: ", year_published))
                deleting_items(found_list, database)

            elif int(option) == 9:
                s = get_status("\nPress Ctrl + d to back\nEnter Status of book to delete: ")
                found_book = []
                for book in database:
                    clearScreen()
                    if s == book[keys[8]]:
                        found_book.append(book)

                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
                
                deleting_items(found_book, database)
                
            else:
                input(color_font("Invalid input please enter 1 to 9", colors.RED))
                continue

            repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter 1 to 4", colors.RED))
            continue

        #Raised when the input() function hits an end-of-file condition (EOF) without reading any data. ctrl + d triggers this error
        except EOFError:
            pass
 


def search_books(database):
    repeat = True
    
    while repeat:
        found_book = []
        clearScreen()
        print(color_font(f"[1] General Search\n[2] Random search\n[3] Search by ISBN\n[4] Search by author\n[5] Search by title \n", colors.BLUE))
        try:
            option = input(color_font("\nSelect option (1-5): ", colors.YELLOW))

            if int(option) == 1:
                
                g = input("\nSearch (any categories): ")
                for book in database:
                    for i in range(len(keys)):
                        if (g.lower() in book[keys[i]].lower()) and (book not in found_book):
                            found_book.append(book)
                            break
                    
                display_books(found_book)
                            

                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
            
            elif int(option) == 2:
                rand = random.choice(database)
                found_book.append(rand)
                clearScreen()
                display_books(found_book)
            
            elif int(option) == 3:
                searching_item(database, key = 1, k = get_ISBN("\nEnter International Standard Book Number (13-digits) to search: "))
                    
            elif int(option) == 4:
                searching_item(database, key = 2, k = get_author("\nEnter author name to search: "))
            
            elif int(option) == 5:
                searching_item(database, key = 3, k = input("\nEnter title of book to search: "))
                
            else:
                input(color_font("Invalid input please enter 1 to 6", colors.RED))
                continue

            repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter 1 to 4", colors.RED))
            continue
        
def get_INDEX(prompt, database):
    while True:
        num = input(prompt)
        for book in database:
            if num == book[keys[0]]:
                return str(num)
           
        print(color_font("No such book exist in database enter valid INDEX.", colors.RED))
        
        
def get_ISBN(prompt):
    while True:
        ISBN = input(prompt)

        if len(ISBN) == 3 and ISBN.isdigit():
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

        if status == "read" or status == "to-read" or status == "reading":
            return str(status)
                 
        else:
            print(color_font("Invalid input. Please enter either \"read\" or \"to-read\" or \"reading\".", colors.RED))
    
    
def display_books(database):
    
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

    for book in database: 
        print(color_font(f"|", colors.GREEN), end="")
        for i in range(len(keys)):
            print("{:^{w}}{}".format(book[keys[i]], colors.GREEN +"|"+colors.ENDC, w=width[i]),end="")
        print()
        
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))
    


def cont_verify(c):
     while True:
        answer = input(c).lower()
        if  answer == "no" or answer == "n":
            return False
        elif answer == "yes" or answer == "y":
            return True
        else:
            input(color_font("Invalid input. Please enter either \"no\" or \"yes\".", colors.RED))
            continue
    
    

def searching_item(database, key, k):
    found_book = []
    for book in database:
        clearScreen()
        if k.lower() in book[keys[key]].lower():
            found_book.append(book)
    
    display_books(found_book)
    if len(found_book) == 0:
        print(color_font("Book was not found", colors.RED))

    return found_book

def deleting_items(found_list, database):
    delete_list = []
    while True:
        
        clearScreen()
        display_books(found_list)
        display_books(delete_list)
        
        print(color_font(f"[1] Select book to delete\n[2] Delete all selected book and exit", colors.BLUE))
        try:
            option = input(color_font("\nSelect option (1 or 2): ", colors.YELLOW))
            if int(option) == 1:
                delete = get_INDEX("\nPlease select index of book you wish to delete (e.g.1): ", database)
                for book in found_list: 
                    if delete == book[keys[0]]:
                        delete_list.append(book)
                        found_list.remove(book)
                            
                if len(delete_list) == 0:
                        input(color_font("Book was not found", colors.RED)) 
                
            elif int(option) == 2:
                for book in delete_list:
                    if book in database:
                        database.remove(book)
                    else:
                        break

                input(color_font("Book(s) was successfuly deleted", colors.GREEN))
                break
                    
            else:
                input(color_font("Invalid input please enter 1 or 2", colors.RED))
                continue

        except ValueError:
            input(color_font("Invalid input please enter integers 1 or 2", colors.RED))
            continue

def show_options():
    print(color_font(f"[1] Add Book Record(s)\n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n", colors.BLUE))

def color_font(text, color):
    return color+text+colors.ENDC

if __name__ == "__main__":
    main()
