# import module
from prettytable import PrettyTable 

# create header
orders = PrettyTable(["OrderNo", "Part1", "Part2", "Part3", "Part4", "Part5"])

# assign data
orders.add_row(["01", "7865", "6425", "9998", "1456", "7115"])
orders.add_row(["02", "4563", "8720", "8016", "1526", "1122"])
orders.add_row(["03", "0098", "7632", "6763", "7886", "0124"])
  
# display table
print("The current orders are as follows:")
print(orders)

# This code uses Memory Profiler. You can use CMD to install Memory Profiler:
# py -m pip install -U memory_profiler
from memory_profiler import profile
@profile
def main():

    # choose option
    choose = input("Would you like to:\n1 - Create a new order\n2 - Delete an existing order\n3 - Modify an existing order\nYour choice: ")

    if choose == "1":
        # create order
        create_orderno = input("Enter the order number: ")
        create_p1 = input("Enter the 4 digit part number for Part 1: ")
        create_p2 = input("Enter the 4 digit part number for Part 2: ")
        create_p3 = input("Enter the 4 digit part number for Part 3: ")
        create_p4 = input("Enter the 4 digit part number for Part 4: ")
        create_p5 = input("Enter the 4 digit part number for Part 5: ")
        orders.add_row([create_orderno, create_p1, create_p2, create_p3, create_p4, create_p5])
        print("Your order has been successfully created! See all orders below:")
        print(orders)

    elif choose == "2":
        delete_index = int(input("Enter the INDEX number of the order you want to delete: "))
        orders.del_row(delete_index)
        print("Your order has been successfully deleted! See all orders below:")
        print(orders)
        
    elif choose == "3":
        # modify order
        modify_index = int(input("Enter the INDEX number of the order you want to modify: "))
        print("This is the order you are modifying: ")

        # print the row selected as preview
        mod = orders.get_string(start=modify_index,end=modify_index+1)
        print(mod)

        # modify the row selected
        mod_orderno = orders.rows[modify_index][0]
        mod_p1 = input("Enter the NEW 4 digit part number for Part 1: ")
        mod_p2 = input("Enter the NEW 4 digit part number for Part 2: ")
        mod_p3 = input("Enter the NEW 4 digit part number for Part 3: ")
        mod_p4 = input("Enter the NEW 4 digit part number for Part 4: ")
        mod_p5 = input("Enter the NEW 4 digit part number for Part 5: ")
        orders.del_row(modify_index)
        orders.add_row([mod_orderno, mod_p1, mod_p2, mod_p3, mod_p4, mod_p5])
        print("Your order has been successfully modified! See all orders below:")
        print(orders)

    else:
        print("You inputted an invalid value")

    # re-run the program at the end
    repeat = input(" \nWould you like to process another order? (yes or no)\nYour input: ")
    if repeat == "yes":
        main()
    else:
        print("End of program")

main()
