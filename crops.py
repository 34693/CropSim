from wheat_class import *
from potato_class import *

def display_menu():
    print()
    print("which crop would you like to create")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please enter a choice from the menu above: ")

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected:: "))
            if choice in (1,2):
                