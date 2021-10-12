import datetime
import json
import random
import csv


def delay(order_id):
    print("-" * 50)
    print("We're sorry for the trouble! Your order will reach you soon.")
    print("Are you satisfied with the solution? \t")
    ch = input("Y/N :")
    if ch == "n" or ch == "N":
        print("-" * 50)
        print("Press 1 to raise a complaint")
        if int(input()) == 1:
            with open("data\\ticket.txt", "a") as ft:
                ticket_num = random.randint(100, 200)
                ft.write(
                    "\n" + str(ticket_num) + "," + order_id + ",delayed"
                )  # writing into csv file
            print("Your complaint has been raised. Your ticket number is ", ticket_num)
        else:
            print("Invalid Input")

    elif ch == "y" or ch == "Y":
        print("Have a nice day, ", name, "!")
        exit
    else:
        print("Invalid input")


def ret_replace(order_id):
    reason = {
        1: "Wrong item delivered",
        2: "Item no longer required",
        3: "Better price available",
        4: "Size too small/large",
        5: "Used product delivered",
        6: "Damaged product",
    }
    print("-" * 50)
    ch = int(input("Choose from the given options\n1. Return\n2. Replace:\n "))

    # return item
    if ch == 1:
        print("-" * 50)
        print("Kindly choose the reason for return")
        for k in reason:
            print(k, reason[k])
        r = int(input("Your answer : "))
        cmt = input("Kindly explain your reason : ")
        addr = input("Will the pick up address be same as delivery address?(Y/N) :")
        if addr == "n" or addr == "N":
            addr = input("Enter the pick up address")

        with open("data\\ticket.txt", "a") as f:
            ticket_num = random.randint(100, 200)
            f.write(
                "\n"
                + str(ticket_num)
                + ","
                + order_id
                + ","
                + "return"
                + ","
                + reason[r]
                + ","
                + cmt
                + ","
                + addr
            )  # writing into csv file

        print("Return has been scheduled. Your ticket number is", ticket_num)
        print("-" * 50)

        pay_method = input("Do you want refund in your original payment method?(Y/N) :")
        if pay_method == "y" or pay_method == "Y":
            print("Amount will be refunded to original payment method")
        elif pay_method == "n" or pay_method == "N":
            print("Amount will be refunded in your wallet")
        else:
            print("Invalid input")

    # replace item
    elif ch == 2:
        print("-" * 50)
        print("Kindly choose the reason for replacement", reason)
        r = int(input("Your answer : "))
        cmt = input("Kindly explain your reason : ")
        addr = input("Will the pick up address be same as delivery address?(Y/N) : ")
        if addr == "n" or addr == "N":
            addr = input("Enter the pick up address")

        with open("data\\ticket.txt", "a") as f:
            ticket_num = random.randint(100, 200)
            f.write(
                "\n"
                + str(ticket_num)
                + ","
                + order_id
                + ","
                + "replace"
                + ","
                + reason[r]
                + ","
                + cmt
                + ","
                + addr
            )  # writing into csv file

        print("Replacement has been scheduled. Your ticket number is", ticket_num)

    else:
        print("Invalid choice")


def damaged(order_id):
    print("-" * 50)
    print("We're sorry for the trouble! We'll do what is best for you.")
    msg = str(input("Kindly tell us more about the damaged product:"))
    print("-" * 50)
    print("That is not acceptable. We'll ensure this doesn't happen again. ")

    ch = input("Do you want to return/replace the item (Y/N): \t")
    if ch == "y" or ch == "Y":
        ret_replace(order_id)

    elif ch == "n" or ch == "N":
        print("Have a nice day, ", name, "!")
        exit
    else:
        print("Invalid input")


def greeting():
    time = datetime.datetime.today()
    if time.hour >= 0 and time.hour < 12:
        print("Good Morning")
    elif time.hour >= 12 and time.hour < 16:
        print("Good Afternoon")
    else:
        print("Good evening")


def check_status():
    ticket = str(input("Please enter the ticket number : "))
    with open("data\\ticket.txt") as f:
        reader = csv.reader(f)
        header = next(reader)
        # take the data from ticket file
        ticket_data = [row for row in reader]

    for i in range(len(ticket_data)):
        if ticket_data[i][0] == ticket:  # compare the ticket number
            with open("data\\products.json") as fj:
                Order_details = json.load(fj)  # read order details from json file
                for k in Order_details:
                    if k == ticket_data[i][1]:
                        print(Order_details[k]["status"])


def raise_new_issue():
    try:
        with open("data\\products.json", "r") as file:
            print("-" * 50)
            print("Your order list:")
            print("Order id\tProduct name")
            # read order details from json file
            Order_details = json.load(file)
            for k, v in Order_details.items() :
                print("{} : \n\tID : {}\n\tOrder Date : {}".format(k, v["id"], v["order_date"]))

        # open file containing order details in json format
        order_id = input("Which product you have concern about?(Enter Order id):")
        while order_id not in Order_details:
            print("This product is not in your list. Kindly enter a valid order id")
            order_id = input()
        print("-" * 50)
        print(
            "Kindly choose from the below options\n1. Delayed Shipping\n2. Damage Product Delivered\n3. Return/Replacement\n"
        )
        choice = int(input())
        # delay shipping
        if choice == 1:
            delay(order_id)
        # damaged product
        elif choice == 2:
            damaged(order_id)
        # return/replace
        elif choice == 3:
            ret_replace(order_id)
        else:
            print("Invalid choice")

    except FileNotFoundError:
        print("You have not ordered any product")
