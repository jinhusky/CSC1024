"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""
# Import necessary modules
import random
import os
import datetime as datetime_s

# Class to define colors for text formatting
class colors:
    # ANSI color codes for different text colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m" # Reset color to default
    BOLD = "\033[1m"

# List of keys representing attributes of a book (const)
keys = ["INDEX", "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]

# Function to print title based on an integer input
def title_GG(n):
    # Nested match expression to select the appropriate title based on the input value
    match n:
        # Cases for different titles based on the input value
        case 0:
            title_ = \
            '''   
  ____              _      __  __                                   
| __ )  ___   ___ | | __ |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
|  _ \ / _ \ / _ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_) | (_) | (_) |   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
|____/ \___/ \___/|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                   |___/         
   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |

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
|____/ \___|\__,_|_|  \___|_| |_|_|_| |_|\__, | |____/ \___/ \___/|_|\_\\n
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
    #create empty databse to be written into everytime program is run
    database = []

    #start counting index to be used in database as a dict at 1
    index = 1
    

    try:
        # Attempt to open the file containing book records (if not found raise FileNotFoundError)
        with open("books_18058073.txt") as txtfile:
            try:
                 # Read each line of the file, splitting the content into individual attributes of a book
                for line in txtfile:
                    ISBN, author, title, publisher, genre, year_published, date_purchased, status = line.rstrip().split(",")
                    # Create a dictionary for each book and append it to the database
                    book = {"INDEX": str(index), "ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
                    database.append(book)
                    index += 1

            #to avoid bug where trying to split an empty line 
            except ValueError:
                pass

    except FileNotFoundError:
        # Notify the user if the file is not found or the path is incorrect
        print(color_font("File not found. Create books.txt or check the file path.", colors.RED))

    prg_end = False 

    #run program until user selects exit option
    while prg_end == False:
        # Display the user interface menu
        clearScreen()
        title_GG(0)
        show_options()

        try:
            # Get the user's option choice
            option = input(color_font("\nSelect option (1-6): ", colors.YELLOW))

            # Perform actions based on the selected option
            if int(option) == 1:
                # Add a book record
                clearScreen()
                title_GG(1)
                add_book(database, index)
                input(color_font("\nBook was successfuly added", colors.GREEN))
                
            
            elif int(option) == 2:
                # Delete a book record
                clearScreen()
                title_GG(2)
                delete_book(database, year_published)
            
            elif int(option) == 3:
                # Update/edit a book record
                clearScreen()
                title_GG(3)
                update_book(database, year_published)

            elif int(option) == 4:
                 # Display all books in the database
                clearScreen()
                title_GG(4)
                display_books(database)
                input()

            elif int(option) == 5:
                # Search for books based on different criteria
                clearScreen()
                title_GG(5)
                search_books(database)
                
            elif int(option) == 6:
                # Exit the program
                clearScreen()
                title_GG(6)
                prg_end = True
                

            elif option == "":
                continue

        except ValueError:
            input(color_font("Invalid input please enter 1 to 6", colors.RED))
            continue

    # Write the updated database to a new file named "new_books.txt"
    with open("books_18058073.txt", "w") as new_file:
        for book in database:
            try:
                # Concatenate book attributes into a string and write to the file
                book_info = ','.join([book['ISBN'], book['Author'], book['Title'], book['Publisher'],
                            book['Genre'], book['Year Published'], book['Date Purchased'], book['Status']])
                
            except TypeError:
                pass
            
            #write the book attribute line by line for each book(the book is a dict in this case) in database
            new_file.write(book_info + "\n")
            


def clearScreen():
    return os.system("cls" if os.name == 'nt' else 'clear')


def add_book(database, index):
    repeat = True
    while repeat:
        # Gather information for a new book
        ISBN = get_ISBN("\nEnter International Standard Book Number (13-digits): ")      
        author = get_author("\nEnter author name: ")
        title = input("\nEnter title of book: ")
        publisher = get_alpha("\nEnter publisher name: ")
        genre = get_alpha("\nEnter book's genre: ")
        year_published = get_year_published("\nEnter the year book was published: ")
        date_purchased = get_date_purchased("\nEnter the date book was purchased (e.g. dd-mm-yyyy): ", year_published)
        status = get_status("\nEnter the status of the book (e.g. 'read' or 'to-read' or 'reading'): ")
        # Create a dictionary for the new book and append it to the database
        book = {"INDEX": str(index),"ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
        
        database.append(book)
        #update the index so that the added new books will be in order
        index += 1

        # Ask the user if they want to continue adding more books
        repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN))) 

    clearScreen()
    # Display the current list of books after adding new entries
    input(display_books(database)) 
    


def delete_book(database, year_published):
    repeat = True
    
    while repeat:
        # Display the user interface menu
        clearScreen()
        title_GG(2)
        display_books(database)
        print(color_font(
            # Display menu options for different deletion methods
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
                # Delete by book index
                k = get_INDEX("\nPress Ctrl + d to back\nEnter INDEX of book to delete: ", database)

                found_book = None
                #if k matches any index of book in database append it the a found_list
                for book in database:
                    clearScreen()
                    if k == book[keys[0]]:
                        found_book = book

                print(found_book)
                #if there is no matches then produce error message
                if found_book == None:
                    print(color_font("Book was not found", colors.RED))
                    pass
                
                repeat = cont_verify((color_font("\n\nDo you wish to delete this book? (e.g. yes/no): ", colors.YELLOW)))
                for book in database:
                    if book == found_book:
                        database.remove(book)
                        display_books(database) 
                        input(color_font("Book(s) was successfuly deleted", colors.GREEN)) 
                
            
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
                #similarly with index have to ensure that status is equivalence to input or else searching read will disply to-read and reading because read is in those str
                s = get_status("\nPress Ctrl + d to back\nEnter Status of book to delete: ")
                found_list = []
                for book in database:
                    clearScreen()
                    if s == book[keys[8]]:
                        found_list.append(book)

                if len(found_list) == 0:
                    print(color_font("Book was not found", colors.RED))
                
                deleting_items(found_list, database)
                
            else:
                input(color_font("Invalid input please enter 1 to 9", colors.RED))
                continue

            repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter intergers only", colors.RED))
            continue

        #Raised when the input() function hits an end-of-file condition (EOF) without reading any data. ctrl + d triggers this error
        except EOFError:
            # pass thru the loop in the middle of entering book details functions as a escape key 
            pass

def search_books(database):
    repeat = True
    
    while repeat:
        found_book = []
        clearScreen()
        title_GG(5)
        # Display search options for the user
        print(color_font(f"[1] General Search\n[2] Random search\n[3] Search by ISBN\n[4] Search by author\n[5] Search by title \n", colors.BLUE))
        try:
            option = input(color_font("\nSelect option (1-5): ", colors.YELLOW))

            if int(option) == 1:
                # General search across all categories
                g = input("\nSearch (any categories): ")
                # Loop through the entire database to find all matches (it is not detailed search)
                for book in database:
                    for i in range(len(keys)):
                        # Check if the search term is in any category and avoid duplicates
                        if (g.lower() in book[keys[i]].lower()) and (book not in found_book):
                            found_book.append(book)
                            break
                clearScreen()
                title_GG(5)
                display_books(found_book)
                            

                if len(found_book) == 0:
                    print(color_font("Book was not found", colors.RED))
            
            elif int(option) == 2:
                # Random book selection
                rand = random.choice(database)
                found_book.append(rand)
                clearScreen()
                title_GG(5)
                display_books(found_book)
            
            elif int(option) == 3:
                # Search by ISBN
                clearScreen()
                title_GG(5)
                searching_item(database, key = 1, k = get_ISBN("\nEnter International Standard Book Number (13-digits) to search: "))
                    
            elif int(option) == 4:
                # Search by author
                clearScreen()
                title_GG(5)
                searching_item(database, key = 2, k = get_author("\nEnter author name to search: "))
            
            elif int(option) == 5:
                # Search by title
                clearScreen()
                title_GG(5)
                searching_item(database, key = 3, k = input("\nEnter title of book to search: "))
                
            else:
                input(color_font("Invalid input please enter 1 to 5", colors.RED))
                continue

            repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter intergers only", colors.RED))
            continue

def update_book(database, year_published):
    # Loop to handle multiple updates until the user decides to exit
    repeat = True
    while repeat:
        clearScreen()
        title_GG(3)
        display_books(database)
        print(color_font(
            "[1] Enter Index of book to update\n"
            "[2] Enter ISBN of book to update\n"
            "[3] Enter author of book to update\n"
            "[4] Enter Title of book to update\n"
            "[5] Enter Publisher of book to update\n"
            "[6] Enter Genre of book to update\n"
            "[7] Enter Year Published of book to update\n"
            "[8] Enter Date Purchased of book to update\n"
            "[9] Enter Status of book to update\n"
            , colors.BLUE))
        
        try:
            option = input(color_font("\nSelect option (1-9): ", colors.YELLOW))
            
            if int(option) == 1:
                # Search and update book by INDEX
                k = get_INDEX("\nPress Ctrl + d to back\nEnter INDEX of book to update: ", database)
                found_list = []
                for book in database:
                    clearScreen()
                    if k == book[keys[0]]:
                        found_list.append(book)
                # Display found books 
                display_books(found_list)
                if len(found_list) == 0:
                    print(color_font("Book was not found", colors.RED))
                #perform the update
                updating_item(found_list, database)
            
            elif int(option) == 2:
                found_list = searching_item(database, key = 1, k = get_ISBN("\nPress Ctrl + d to back\nEnter International Standard Book Number (13-digits) to update: "))
                updating_item(found_list, database)

            elif int(option) == 3:
                found_list = searching_item(database, key = 2, k = get_author("\nPress Ctrl + d to back\nEnter Author of book to update: "))
                updating_item(found_list, database)

            elif int(option) == 4:
                found_list = searching_item(database, key = 3, k = input("\nPress Ctrl + d to back\nEnter Title of book to update: "))
                updating_item(found_list, database)

            elif int(option) == 5:
                found_list = searching_item(database, key = 4, k = get_alpha("\nPress Ctrl + d to back\nEnter Publisher of book to update: "))
                

            elif int(option) == 6:
                found_list = searching_item(database, key = 5, k = get_alpha("\nPress Ctrl + d to back\nEnter Genre of book to update: "))
                updating_item(found_list, database)

            elif int(option) == 7:
                found_list = searching_item(database, key = 6, k = get_year_published("\nPress Ctrl + d to back\nEnter Year Published of book to update: "))
                updating_item(found_list, database)

            elif int(option) == 8:
                found_list = searching_item(database, key = 7, k = get_date_purchased("\nPress Ctrl + d to back\nEnter Date Purchased of book to update: ", year_published))
                updating_item(found_list, database)

            elif int(option) == 9:
                s = get_status("\nPress Ctrl + d to back\nEnter Status of book to update: ")
                found_list = []
                for book in database:
                    clearScreen()
                    if s == book[keys[8]]:
                        found_list.append(book)

                if len(found_list) == 0:
                    print(color_font("Book was not found", colors.RED))
                
                updating_item(found_list, database)
                
            else:
                input(color_font("Invalid input please enter 1 to 9", colors.RED))
                continue

             # Asking if the user wants to continue updating
            repeat = cont_verify((color_font("\n\nDo you wish to continue? (e.g. yes/no): ", colors.GREEN)))

        except ValueError:
            input(color_font("Invalid input please enter interger 1 to 9", colors.RED))
            continue

        #Raised when the input() function hits an end-of-file condition (EOF) without reading any data. ctrl + d triggers this error
        except EOFError:
            pass
            


def get_INDEX(prompt, database):
    # Function to get and validate the INDEX of a book in the database
    while True:
        num = input(prompt)
        # Iterate through the database to check if the INDEX exists
        for book in database:
            if num == book[keys[0]]:
                return str(num)
            
        # If the INDEX doesn't exist in the database, prompt for a valid INDEX
        print(color_font("No such book exist in database enter valid INDEX.", colors.RED))
        
        
def get_ISBN(prompt):
    # Function to get and validate the ISBN of a book
    while True:
        ISBN = input(prompt)

        # Check for a 13-digit ISBN which contains only digits
        if len(ISBN) == 13 and ISBN.isdigit():
            return str(ISBN)
        else:
             # Prompt if the ISBN is not a valid 13-digit number
            print(color_font("Invalid input. Please enter a 13-digit number.", colors.RED))

def get_author(prompt):
    # Function to get and validate the author's name
    while True:
        author = input(prompt)

        # Check if the author's name contains only alphabets, spaces, and dots
        if all(char.isalpha() or char.isspace() or char == '.' for char in author):
           
            return str(author.title())
        
        else:
            print(color_font(f"Invalid input. Please enter only alpha \".\" for author's name.", colors.RED))

def get_alpha(prompt):
     while True:
        author = input(prompt)
        # Check if the input string contains only alphabets and spaces
        if all(char.isalpha() or char.isspace() for char in author):
            return str(author.title())
        else:
            print(color_font(f"Invalid input. Please enter only alphabets.", colors.RED))

def get_year_published(prompt):
    # Function to get and validate the year of book publication
    while True:
        try:
            year = int(input(prompt))
            current_year = datetime_s.datetime.now().year
            # Validate if the entered year is within a valid range
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
            # Validate if the entered date is within a valid range
            if date_obj > datetime_s.datetime.now() or date_obj.year < int(year_published):
                print(color_font(f"Invalid input. Cant purchase books in the future (dd-mm-yyyy): ", colors.RED))
                continue

            return str(date_obj.strftime("%d-%m-%Y"))
        
        except ValueError:
            print(color_font(f"Invalid input. Please enter the date in the format (dd-mm-yyyy): ", colors.RED))

def get_status(prompt):
    while True:
        status = input(prompt)
        # Check if the entered status matches predefined values
        if status == "read" or status == "to-read" or status == "reading":
            return str(status)
                 
        else:
            print(color_font("Invalid input. Please enter either \"read\" or \"to-read\" or \"reading\".", colors.RED))
    
    
def display_books(database):
    # Function to display the books in a formatted table
    # Calculating the width required for each column

    #this width is default to avoid bug when given argument(list) is empty
    width = [5, 13, 8, 7, 11, 7, 16, 16, 8]
    for book in database: 
        for key in keys:
            #finding the maximum len for each attribute of book in database
            if width[keys.index(key)] < len(book[key]):
                width[keys.index(key)] = len(book[key])      

    #printing the borders of the table 
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))

    index = 0
    print(color_font(f"|", colors.GREEN), end="")

    # Printing the header of the table
    for i in keys:
        print("{:^{w}}{}".format(i, colors.GREEN +"|"+colors.ENDC, w=width[index]), end="")
        index += 1

    print()
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))

    # Printing each book's information row by row
    for book in database: 
        print(color_font(f"|", colors.GREEN), end="")
        for i in range(len(keys)):
            print("{:^{w}}{}".format(book[keys[i]], colors.GREEN +"|"+colors.ENDC, w=width[i]),end="")
        print()
        
    print(color_font(f"="*(sum(width)+10)+"", colors.GREEN))
    
def cont_verify(c):
     # Function to verify continuation based on user input
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
    # Function to search for items in the database based on a specific key and value
    found_book = []
    for book in database:
        if k.lower() in book[keys[key]].lower():
            found_book.append(book)

    # Display the found books and return the list
    display_books(found_book)
    if len(found_book) == 0:
        print(color_font("Book was not found", colors.RED))

    return found_book

def deleting_items(found_list, database):
    # Function to delete selected items from the database
    delete_list = [] # List to store books selected for deletion
    while True:

        clearScreen()
        display_books(found_list)
        display_books(delete_list)
        
        # Providing options for deleting books
        print(color_font(f"[1] Select book to delete\n[2] Delete all selected book and exit", colors.BLUE))
        try:
            option = input(color_font("\nSelect option (1 or 2): ", colors.YELLOW))
            if int(option) == 1:
                delete = get_INDEX("\nPlease select index of book you wish to delete (e.g.1): ", database)
                #if selected index matches the index in the found_list transfer book to delete_list
                for book in found_list: 
                    if delete == book[keys[0]]:
                        delete_list.append(book)
                        found_list.remove(book)
                            
                if len(delete_list) == 0:
                        input(color_font("Book was not found", colors.RED)) 
            
            #Once user has selected all the book(s) they wish the delete from found_list proceed to delete books from database
            elif int(option) == 2:
                for book in delete_list:
                    if book in database:
                        database.remove(book)  # Remove selected books from the main database
                    else:
                        break # Exit the loop if a book is not found in the main database

                input(color_font("Book(s) was successfuly deleted", colors.GREEN))
                break # Exit the loop after deletion
                    
            else:
                input(color_font("Invalid input please enter 1 or 2", colors.RED))
                continue  #Continue the loop for input until a valid option is chosen

        except ValueError:
            input(color_font("Invalid input please enter integers 1 or 2", colors.RED))
            continue # Continue the loop for input until a valid integer is entered


def updating_item(found_list, database):
    while True:
        clearScreen()
        display_books(found_list)
        
        try:
            index = int(input(color_font(f"Enter index of book you want to update/edit: ", colors.BLUE)))
            updating_book = None
            
             # Check if the provided index exists in the found_list
            for book in found_list:
                if index == int(book[keys[0]]):
                    updating_book = book
                    print(updating_book)

        # If the book is not found in the provided list, prompt the user for correct input                      
        except ValueError:
            input(color_font("Invalid input only accept integers of INDEX", colors.RED))
            continue

        if updating_book == None:
            input(color_font("Input correct INDEX of book in update list", colors.RED))
            continue

        # Gather updated information for the book
        ISBN = get_ISBN(f"\nEnter New ISBN (Old:{updating_book[keys[1]]}): ")
        author = get_author(f"\nEnter new author name (Old:{updating_book[keys[2]]}): ")
        title = input(f"\nEnter new title (Old:{updating_book[keys[3]]}): ")
        publisher = get_alpha(f"\nEnter new publisher name (Old:{updating_book[keys[4]]}): ")
        genre = get_alpha(f"\nEnter book's new genre (Old:{updating_book[keys[5]]}): ")
        year_published = get_year_published(f"\nEnter the year book was published (Old:{updating_book[keys[6]]}): ")
        date_purchased = get_date_purchased(f"\nEnter the date book was purchased (Old:{updating_book[keys[7]]}): ", year_published)
        status = get_status(f"\nEnter the status of the book (Old:{updating_book[keys[8]]}): ")

        # Create a new book entry with updated information
        new_book = {"INDEX": updating_book[keys[0]],"ISBN": ISBN, "Author": author, "Title": title, "Publisher": publisher
                                    , "Genre": genre, "Year Published": year_published, "Date Purchased": date_purchased, "Status": status}
        
        # Replace the old book entry with new book entry in the main database based on the index
        database[int(updating_book[keys[0]])] = new_book
        input(color_font("Book(s) was successfuly updated", colors.GREEN))
        return
        
def show_options():
    print(color_font(f"[1] Add Book Record(s)\n[2] Delete Book Record(s)\n[3] Update/Edit Book Record(s)\n[4] Display\n[5] Search\n[6] Exit\n", colors.BLUE))

def color_font(text, color):
    return color+text+colors.ENDC

if __name__ == "__main__":
    main()
