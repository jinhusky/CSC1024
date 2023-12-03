def get_int(num):
    while True:
        try:
            number = int(input(num))
            
        except ValueError:
            print("Invalid input, please enter a valid number!")
            continue
    
        return number