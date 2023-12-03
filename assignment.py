"""
CSC1024 Programming Principles Final Assessment Project
A Personal Book Management System using Python
Date : 27 Nov 2023
"""

import random
import os
import datetime

def main():

    options_menu = get_int("Select option: ")




def get_int(num):
    while True:
        try:
            option = int(input(num))
        
        except ValueError:
            print("Please enter a number !")
            continue
    
        return option

def show_menu():
    print(f"[1] Add Book Record(s)\n [2] Update/Edit Book Record(s)\n [3] Update/Edit Book Record(s) [4] Display [5] Search [6] Exit")
          


    
if __name__ == "__main__":
    main()