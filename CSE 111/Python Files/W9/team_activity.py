import csv

def main():
    
    dictionary = read_dict('students.csv')
    print(dictionary)
    i_number = input("What is your I-Number? ")
    get_student(i_number, dictionary)
    
    

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)

        for rows in reader:
            k, v = rows
            dictionary[k] = v
    
    return dictionary

def get_student(i_number, filename ):
    if i_number in filename:
        print(filename[i_number])
    else:
        print("No such student")

    

if __name__ == "__main__":
    main()