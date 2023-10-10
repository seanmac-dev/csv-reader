import csv


def main():
    user_input = input("What type of animal would you like to see info about?")

    if user_input == "cat":
        with open("./data/cats.csv", "r") as file:
            cat_file = csv.reader(file)
            for lines in cat_file:
                print(lines)
    elif user_input == "dog":
        with open("./data/dogs.csv", "r") as file:
            dog_file = csv.reader(file)
            for lines in dog_file:
                print(lines)
    else:
        print("Sorry, we don't have those types of animals.")


main()

# name, age, breed
# loki, 6, shorthair
# shadow, 3, siamese
# garfield, 2, ocelot

# User input (type of animal) --> cat | dog
# Displays info from csv:
#   [open method] to read csv file
#   [csv module] to parse data into [] | {}
# Output ex. "fido is a 4 year old husky."
# Try/except to handle bad input:
#   Display error msg

# If we have time: STRETCH close file [with statement]
