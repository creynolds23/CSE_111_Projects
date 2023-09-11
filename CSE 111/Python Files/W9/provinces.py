"""
Author: Conner Reynolds
Purpose: Add and Edit a txt file
Date: 11/9/22
"""

def main():
    # Open contents of the txt file into a list
    provinces_list = read_list("provinces.txt")

    # Print List
    print(provinces_list)

    # #Remove first element from list
    provinces_list.pop(0)

    # #Remove last element from list
    provinces_list.pop()


    #Replace AB with Alberta
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    #Find how many Albertas there are
    count = provinces_list.count("Alberta")

    print()
    print(f'Alberta occurs {count} times in the modified list.')


def read_list(filename):
    # Start list with empty brackets
    text_list = []

    # Open text file
    with open(filename, "rt") as text_file:
        # Read contents of file
        for line in text_file:

            #Remove white space
            clean_line = line.strip()

            # Append clean line of text
            text_list.append(clean_line)
        
    return text_list

if __name__ == "__main__":
    main()