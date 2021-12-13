# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
# Create a function called "save_csv" in order to save the qualifying loan in app.py as a CSV file.
def save_csv(path, new_data):
    # Open the output CSV file path using 'with open'
    with open(path, "w") as csvfile:
        # Create a csvwriter
        csvwriter = csv.writer(csvfile, delimiter="," )
        # Use a for loop to interate through each "row" in the "new_data" csv file
        for row in new_data:
            # Writing a new row using csvwriter for each row in "new_data" csv file
            csvwriter.writerow(row)