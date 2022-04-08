#!/usr/bin/env python3

def read_file(filename):
    """
        Opens the named file and returns a list of strings,
        one for each line in the file
    """
    # This is fake for now
    lines = []
    return lines

def build_car_dictionary(lines):
    """
        Given a list of strings in the format of each line of the CSV file,
        produce the car dictionary 
    """
    # Hardcoded for now
    car_dictionary = {
        "70 chevrolet chevelle malibu":
            [ 18, 8, 307, 130, 3504, 12, 70, "usa", "chevrolet chevelle malibu" ],
        "70 buick skylark 320":
            [ 15, 8, 350, 165, 3693, 11.5, 70, "usa", "buick skylark 320" ],
        "70 plymouth satellite":
            [ 18, 8, 318, 150, 3436, 11, 70, "usa", "plymouth satellite" ],
        "70 amc rebel sst":
            [ 16, 8, 304, 150, 3433, 12, 70, "usa", "amc rebel sst" ],
    }

    return car_dictionary

def best_mpg(parameter1, parameter2):
    pass

def worst_mpg(parameter1, parameter2):
    pass

def average_mpg(parameter1, parameter2):
    pass

def print_models_above(parameter1, parameter2, parameter3):
    pass

def print_models_below(parameter1, parameter2, parameter3):
    pass

def get_menu_choice_from_user():
    """
        Print the menu, collect the user's choice, and validate it.
        Returns 0 when the choice was not valid.
    """
    print("(1) Get best mpg by country")
    print("(2) Get worst mpg by country")
    print("(3) Get average mpg by country")
    print("(4) Print models above threshold")
    print("(5) Print models below threshold")
    print("(6) Exit")
    print("Enter selection 1-6:")

    user_input = input()
    # Have to check if it's a number or int() will throw an error
    if user_input.isdigit():
        menu_choice = int(user_input)
        if menu_choice >= 1 and menu_choice <= 6:
            return menu_choice
    
    print("Invalid selection - must be a number from 1 to 6")
    return 0

def get_country_from_user():
    """
        Collect a country from the user. If the country is not in the list
        of valid countries, print an error and return an empty string.
    """
    # "Europe" isn't a country >:(
    valid_countries = [ "usa", "japan", "europe" ]

    print("Enter country of origin:")
    chosen_country = input()
    if chosen_country not in valid_countries:
        print(f"{chosen_country} is not a country in this data")
        chosen_country = ""

    return chosen_country

def get_menu_choice_and_country_from_user():
    """
        Collect the menu choice and country from the user. Keep asking
        until valid choices of both have been made.
    """
    menu_choice = 0
    chosen_country = ""

    # Keep asking the user for input until both fields are valid;
    # also have to consider that when the user chooses 6, we won't ask
    # for country, which leaves it blank but we are still done.
    while menu_choice == 0 or (menu_choice != 6 and chosen_country == ""):
        menu_choice = get_menu_choice_from_user()
        # Only ask country if the menu_choice was valid or if we're not exiting
        if menu_choice != 0 and menu_choice != 6:
            chosen_country = get_country_from_user()

    return menu_choice, chosen_country

def get_filename():
    """
        Prompt the user and collect a filename from them
    """
    print("Enter the filename:")
    filename = input()

    return filename

# -------- MAIN --------

filename = get_filename()
lines = read_file(filename)
car_dictionary = build_car_dictionary(lines)

menu_choice = 0
while menu_choice != 6:
    menu_choice, chosen_country = get_menu_choice_and_country_from_user()
