#!/usr/bin/env python3

def read_file(filename):
    """
        Opens the named file and returns a list of strings,
        one for each line in the file.
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # Remove the first line because it's a header
    lines = lines[1:]

    # lines is a list of strings, but each one ends with a newline we don't want;
    # chop off the last character
    trimmed_lines = []
    for line in lines:
        trimmed_lines.append(line[:-1])
    
    return trimmed_lines

def build_car_dictionary(lines):
    """
        Given a list of strings in the format of each line of the CSV file,
        produce the car dictionary.
    """
    car_dictionary = {}

    for line in lines:
        columns = line.split(",")
        model_year = columns[6]
        model = columns[8]
        key = f"{model_year} {model}"

        # The instructions say you can't include values in the list that were
        # in the key or some tests will fail. This is not true. No function
        # returns the dictionary, so there's no way for a test to examine it
        # for extra data, and all the functions return the right values whether
        # or not the extra fields are there. But I'll take them out because a
        # person examining the code could see that there are extra values.
        # Hence the following two lines. Pfft.
        del columns[8] 
        del columns[6] 

        car_dictionary[key] = columns
    
    return car_dictionary

# Do parameters like this need to be literally "parameter1" and "parameter2"
# like in the instructions?
def best_mpg(car_dictionary, country):
    """
        Given the car dictionary and country, returns the mpg of the
        highest-mpg car in the dictionary that is in that country.
    """
    best_mpg = -9999.0
    for value in car_dictionary.values():
        current_country = value[6]
        if current_country == country:
            current_mpg = float(value[0])
            if current_mpg > best_mpg:
                best_mpg = current_mpg

    return best_mpg

def worst_mpg(car_dictionary, country):
    """
        Given the car dictionary and country, returns the mpg of the
        lowest-mpg car in the dictionary that is in that country.
    """
    worst_mpg = 9999.0
    for value in car_dictionary.values():
        current_country = value[6]
        if current_country == country:
            current_mpg = float(value[0])
            if current_mpg < worst_mpg:
                worst_mpg = current_mpg

    return worst_mpg

def average_mpg(car_dictionary, country):
    """
        Given the car dictionary and country, returns the average mpg
        of all the cars manufactured in that country.
    """
    total_mpg = 0.0
    number_of_cars = 0
    for value in car_dictionary.values():
        current_country = value[6]
        if current_country == country:
            current_mpg = float(value[0])
            total_mpg += current_mpg
            number_of_cars += 1

    return total_mpg / number_of_cars


def print_models_above(car_dictionary, country, min_mpg):
    """
        Prints a report of all the models in the dictionary having
        an mpg higher than the requested mpg in the provided country.
    """
    print(f"Models from {country} with {min_mpg:.2f} or better:")
    print(f"Model                                    Weight     Horsepower    Miles Per Gallon")
    print("-" * 82)
    
    for key, value in car_dictionary.items():
        current_country = value[6]
        if current_country == country:
            model = key
            weight = value[4]
            horsepower = value[3]
            mpg = float(value[0])
            if (mpg >= min_mpg):
                print(f"{model:<40}{weight:>7}{horsepower:>15}{mpg:>20.2f}")

def print_models_below(car_dictionary, country, max_mpg):
    """
        Prints a report of all the models in the dictionary having
        an mpg higher than the requested mpg in the provided country.
    """
    print(f"Models from {country} with {max_mpg:.2f} or lower:")
    print(f"Model                                    Weight     Horsepower    Miles Per Gallon")
    print("-" * 82)
    
    for key, value in car_dictionary.items():
        current_country = value[6]
        if current_country == country:
            model = key
            weight = value[4]
            horsepower = value[3]
            mpg = float(value[0])
            if (mpg <= max_mpg):
                print(f"{model:<40}{weight:>7}{horsepower:>15}{mpg:>20.2f}")

def get_min_mpg_from_user():
    print("Enter the mpg value models must be at or over:")
    return float(input())

def get_max_mpg_from_user():
    print("Enter the mpg value models must be at or under:")
    return float(input())

def get_menu_choice_from_user():
    """
        Print the menu, collect the user's choice, and validate it.
        Returns 0 when the choice was not valid.
    """
    print()
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

def get_filename_from_user():
    """
        Prompt the user and collect a filename from them
    """
    print("Enter the filename:")
    filename = input()

    return filename

# -------- MAIN --------

filename = get_filename_from_user()
lines = read_file(filename)
car_dictionary = build_car_dictionary(lines)

menu_choice = 0
while menu_choice != 6:
    menu_choice, chosen_country = get_menu_choice_and_country_from_user()

    if menu_choice == 1:
        best = best_mpg(car_dictionary, chosen_country)
        # This output string isn't in the instructions, only an example
        print(f"Best mpg from {chosen_country} is {best:.2f}")

    elif menu_choice == 2:
        worst = worst_mpg(car_dictionary, chosen_country)
        # This output string isn't in either the instructions or an example;
        # have to assume what it's supposed to be and see what the tests say.
        print(f"Worst mpg from {chosen_country} is {worst:.2f}")

    elif menu_choice == 3:
        average = average_mpg(car_dictionary, chosen_country)
        # This output string isn't in the instructions, only an example
        print(f"Average mpg from {chosen_country} is {average:.2f}")

    elif menu_choice == 4:
        min_mpg = get_min_mpg_from_user()
        print_models_above(car_dictionary, chosen_country, min_mpg)

    elif menu_choice == 5:
        max_mpg = get_max_mpg_from_user()
        print_models_below(car_dictionary, chosen_country, max_mpg)