from prettytable import PrettyTable
import random
import string
import sys

materiales_dic = {}

# ~~~~~~~~~~~~~~~~~~ Functions(): ~~~~~~~~~~~~~~~~~~~
def main():
    # ~~~~~~~~~~~~~~ User's choise ~~~~~~~~~~~~~~~
    while True:
        instrucctions()
        user_input = input("\nWhat do you want to do? "
                           "(a, d, u, l, e): ").lower()
        if user_input == "a":
            add_materiales()
        elif user_input == "d":
            delete_materiales()
        elif user_input == "u":
            update_materiales()
        elif user_input == "l":
            print_register()
        elif user_input == "e":
            exit_program()
        elif not user_input:
            print("please, enter something!")

# ~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~
def instrucctions():
    print('\n Registro de proformas y materiales : '
          '\n1: Enter A or a to add new materiales.'
          '\n2: Enter D or d to delete a materiales'
          '\n3: Enter U or u to update materiales.'
          '\n4: Enter L or l to check list of materialess. '
          '\n5: Enter E or e to exit the program.')
    
def print_register():
    x = PrettyTable(["ID", "Cod1 ", "Cod2", "Des", "Uni", "CCF-Can", "CCD-Sup", "V1CF-CMO", "V1CD-CAC", "V2CF-CVI", "V2CD-CTOT", "Obs", "AcCan", "AcMet", "AcCCF","AcCCD"])
    for materiales_data in materiales_dic:
        x.add_row([materiales_data, 
                   materiales_dic[materiales_data]["Cod1"],
                   materiales_dic[materiales_data]["Cod2"],
                   materiales_dic[materiales_data]["Des"],
                   materiales_dic[materiales_data]["Uni"],
                   materiales_dic[materiales_data]["CCF-Can"],
                   materiales_dic[materiales_data]["CCD-Sup"],
                   materiales_dic[materiales_data]["V1CF-CMO"],
                   materiales_dic[materiales_data]["V1CD-CAC"],
                   materiales_dic[materiales_data]["V2CF-CVI"],
                   materiales_dic[materiales_data]["V2CD--CTOT"],
                   materiales_dic[materiales_data]["Obs"],
                   materiales_dic[materiales_data]["AcCan"],
                   materiales_dic[materiales_data]["AcMet"],
                   materiales_dic[materiales_data]["AcCCF"],
                   materiales_dic[materiales_data]["AcCCD"]])
    print(x.get_string(title="materiales registry"))

for materiales_data in materiales_dic:
    x.add_row([materiales_data, materiales_dic[materiales_data]["scientific_name"], materiales_dic[materiales_data]["common_name"]])
    print(x.get_string(title="materiales registry"))

def random_id():
    random_string = ''.join(random.choices(string.ascii_uppercase
                                           + string.digits, k=4))
    return random_string

def add_materiales():
    materiales_id = random_id()
    scientific_name = input("\nPlease enter the scientific name: ").title()
    common_name = input("\nPlease enter the common name: ").title()
    data = {materiales_id: {'scientific_name': scientific_name,
                        'common_name': common_name}}
    if not scientific_name and not common_name:
        print("You must write something!")
    else:
        materiales_dic.update(data)

def delete_materiales():
    materiales_id = input("\nEnter the materiales ID you want delete: ").upper()
    if materiales_id in materiales_dic:
        choice = input("Delete (y/n)").lower()
        if choice == "yes" or choice == "y":
            del materiales_dic[materiales_id]
            print(f"{materiales_id} registry has been deleted!")
    else:
        print("ID not found. Check list pressing 'L'")

def update_materiales():
    materiales_id = input("\nEnter the materiales ID you want update: ").upper()
    # If external key in dictionary, if key is equal to ID (materiales_id)
    for materiales in materiales_dic:
        if materiales == materiales_id:
            choice = input(f"Update registry {materiales_id}? (y/n): ").lower()
            if choice == "yes" or choice == "y":
                # Changing names
                scientific_name = input("Write a new scientific name: ").title()
                common_name = input("Write a new common name: ").title()
                if not scientific_name and not common_name:
                    print("You must write something!")
                else:
                # Updating
                    materiales_dic[materiales]['scientific_name'] = scientific_name
                    materiales_dic[materiales]['common_name'] = common_name
                    print("registry updated!")
                    print_register()
        else:
            print("ID not found. Check list pressing 'L'")

def exit_program():
    sys.exit("Goodbye!")

if __name__ == "__main__":
    main()
