import sys
import os
import pandas as pd

# Functions
## Make sure file name is given when executing python program
def file_check():
    file_path = sys.argv[1]
    if len(sys.argv) != 2:
        print("Usage: python csv_reader.py <path_to_csv_file>")
        sys.exit(1)
    if not os.path.isfile(file_path) or not file_path.endswith('.csv'):
        print("Error: The file must exist and be a CSV file.")
        sys.exit(1)
    print(f"Processing file: {file_path}")
    return file_path

## Read in the csv file, print csv headers, give one-line example of data in the file
def read_and_show_example(file_path):
    with open(file_path, mode = 'r') as file:
        return file
    
## Have user select what headers he wants to extract and in what order

## Ask for out_file path/name

## Create new csv file that is filtered exactly the way the user wants the data formated (in csv)

# Main program
def main():
    print("Hello, world!")


if __name__ == "__main__":
    main()