import csv
from datetime import datetime

PRODUCT_NAME = 0
PRICING = 1

def main():
    PRODUCT_KEY = 0
    PRODUCT_AMOUNT = 1
    total_items = 0
    pre_tax = 0
    print("Walmart")
    products = read_products("products.csv")
    date_time = datetime.now()
    try:
        with open("request.csv", "rt") as requests:
            reader = csv.reader(requests)
            next(reader)
            print()
            print("Requested Items")
            for row in reader:
                key = row[PRODUCT_KEY]
                amount = int(row[PRODUCT_AMOUNT])
                product = products[key]
                name = product[PRODUCT_NAME]
                price = product[PRICING]
                total_items += amount
                amount_cost = amount * price
                pre_tax += amount_cost
                print(f"{name}: {amount} @ {price}")
            print()
            tax = pre_tax * 0.06
            final_price = pre_tax + tax
            print(f"Number of items: {total_items}")
            print(f"Subtotal: {pre_tax:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: {final_price:.2f}")
            print()
            print("Thank you for shopping at Walmart.")
            print(f"{date_time:%a %b %d %H:%M:%S %Y} ")
    except FileNotFoundError as file_error:
        print(file_error)
    except PermissionError as perm_error:
        print(perm_error)
    except KeyError as key:
        print(key)
        

def read_products(filename):
    dictionary = {}
    with open(filename, "rt") as products:
        reader = csv.reader(products)
        next(reader)
        for row in reader:
            key = row[0]
            name = row[1]
            price = row[2]
            dictionary[key] = name, float(price)
    return dictionary




if __name__ == "__main__":
    main()