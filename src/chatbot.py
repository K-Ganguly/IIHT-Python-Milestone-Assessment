import datetime
import json
import random
import csv

from chatbot_utils import *


if __name__ == "__main__":
    greeting()
    name = input("Enter your name : ")
    print(
        "Hello {}, we hope you are doing well.\nWhat can we help you with ? \n".format(
            name
        )
    )

    while 1:
        print("\nEnter 1 to check the status of an already raised issue.")
        print("Enter 2 to raise a new issue.")
        print("Enter 3 to exit\n")
        print("-" * 50)
        try:
            response = int(input())
        except ValueError:
            print("Invalid input")

        else:
            # check the status of an already raised ticket
            if response == 1:
                check_status()

            # raise a new concern
            elif response == 2:
                raise_new_issue()

            # exiting
            elif response == 3:
                print("Have a nice day!")
                break
            else:
                print("Sorry! That's not a valid option.")

        finally:
            pass
