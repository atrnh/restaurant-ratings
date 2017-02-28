"""Print restaurant ratings.

Reads restaurant names and ratings from a file supplied by a command line argument. Allows user to
add restaurants, update ratings of existing restaurants, and update the ratings of a random
argument.

Gives user the option of printing an alphabetized list of the restaurants and their ratings to the
console.
"""

import sys
import random


ratings = {}

def titleize_name(name):
    """Returns the titleized restaurant name.

    Example:
        titleize_name('the good restaurant')
        >>> 'The Good Restaurant'
    """

    words = name.split()

    for idx, word in enumerate(words):
        words[idx] = word[0].upper() + word[1:]

    return ' '.join(words)


def get_ratings_from_file(ratings):
    """Set restaurants and ratings from file as key value pairs."""

    file_name = sys.argv[1]
    ratings_file = open(file_name)

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(":")
        ratings[titleize_name(restaurant)] = int(rating)


def print_restaurant_ratings(ratings):
    """Prints restaurants in alphabetical order with their ratings."""

    for restaurant, rating in sorted(ratings.items()):
        print '%s is rated at %d' % (restaurant, rating)


def get_ratings_from_user(ratings):
    """Prompts users for restaurants and ratings.

    Sets restaurant and ratings as key value pairs to supplied dictionary.
    """

    restaurant = raw_input("Enter the name of the restaurant: ")
    rating = int(raw_input("Enter the rating of the restaurant: "))

    ratings[titleize_name(restaurant)] = rating


def prompt_user(ratings):
    """This runs the restaurant-ratings program."""

    while True:
        print "Would you like to:"
        print "1. Add another restaurant"
        print "2. Update the rating for a random restaurant"
        print "3. Update the rating of a restaurant"
        print "4. Quit"
        user_choice = raw_input("Enter a number: ")

        if user_choice == "1":
            get_ratings_from_user(ratings)
        elif user_choice == "2":
            update_random_restaurant(ratings)
        elif user_choice == "3":
            update_restaurant(ratings)
        elif user_choice == "4":
            print_result = raw_input("Do you want to print the result? y/n ").lower()

            if print_result == 'y':
                print
                print_restaurant_ratings(ratings)
                break
            elif print_result == 'n':
                break
            else:
                print "Restaurants will not be printed."
                break
        else:
            print "Invalid input."
            continue


def update_random_restaurant(ratings):
    """Update a random restaurant."""

    rand_restaurant = random.choice(ratings.keys())
    print "The random restaurant is: %s" % rand_restaurant
    rating = int(raw_input("Please enter a new rating: "))

    ratings[rand_restaurant] = rating


def update_restaurant(ratings):
    """Update a named restaurant."""

    restaurant = raw_input("Which restaurant would you like to update? ")

    if restaurant not in ratings:
        print "Warning: new restaurant is being added."

    rating = int(raw_input("Enter a new rating: "))

    ratings[titleize_name(restaurant)] = rating


get_ratings_from_file(ratings)
prompt_user(ratings)
