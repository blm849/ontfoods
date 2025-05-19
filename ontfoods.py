# This program determines what food is fresh in Ontario for any month.
# The user provides the name of the month, and then this program reads the input_file
# and finds all foods that are fresh in that month.
# The input file looks like this:
'''
Maple syrup,YearRound,,,,,,,,,,,
Milk & milk products,YearRound,,,,,,,,,,,
Mushrooms,YearRound,,,,,,,,,,,
Muskmelon,Aug,Sep,,,,,,,,,,
Mustard Greens (Gai Choy),Jun,Jul ,Aug,Sep,Oct,,,,,,,
Nappa Cabbage,Jun,Jul ,Aug,Sep,Oct,Nov,,,,,,
Nectarines,Aug,Sep,,,,,,,,,,
Onions (Cooking),YearRound,,,,,,,,,,,
'''
# If a food is fresh for a given month (e.g. Aug), the program will print out the food
# (e.g. Nectarines). If a food is fresh YearRound (e.g. Mushrooms), it will print it out
# if seasonal is set to False. If it is set to True, it will not print out the YearRound
# foods

import csv

input_file = "ontfoods.csv"
seasonal = True

def find_foods_by_month(month):
    results = []

    # Normalize input month
    month = month.strip().capitalize()

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Clean up whitespace
            normalized_row = [cell.strip() for cell in row]
            if seasonal:
                if month in normalized_row:
                    first_item = normalized_row[0]
                    results.append(first_item)
            else:
                if month in normalized_row or "YearRound" in normalized_row:
                    first_item = normalized_row[0]
                    if "YearRound" in normalized_row:
                        first_item = first_item + "*"
                    results.append(first_item)  # First column = food name

    return results


# Begin the program. Ask the user for the month they want fresh food information on.
# (Months are Jan Feb Mar Apr May etc.). Then find the fresh food for that month and 
# print it out:

if __name__ == "__main__":
    input_month = input("Enter month (e.g., Aug): ")
    fresh_foods = find_foods_by_month(input_month)

    print("\nFresh food for", input_month,":")
    for food in fresh_foods:
        print("-", food)
