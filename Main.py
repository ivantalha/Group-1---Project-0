# Main Python File to run from
from ContactArray import ContactList
from Contact import Contact

MENUS = {
    "main": {
        1: "Store to ASEAN Phonebook",
        2: "Edit entry in ASEAN Phonebook",
        3: "Delete entry from ASEAN Phonebook",
        4: "View/Search ASEAN Phonebook",
        5: "Exit"
    },
    "views": {
        1: "Search by country",
        2: "Search by surname",
        3: "View all",
        4: "Go back to main menu"
    },
    "edit": {
        1: "Student Number",
        2: "Surname",
        3: "Gender",
        4: "Occupation",
        5: "Country Code",
        6: "Area Code",
        7: "Phone Number",
        8: "None - Go back to main menu"
    },
    "cc": {
        1: "Burma", # 856
        2: "Cambodia", # 855
        3: "Thailand", # 66
        4: "Vietnam", # 84
        5: "Malaysia", # 60
        6: "Philippines", # 63
        7: "Indonesia", # 62
        8: "Timor Leste", # 670
        9: "Laos", # 95
        10: "Brunei", # 673
        11: "Singapore", #65
        12: "All",
        0: "No More"
    }
}

def showMenu(target: str, inline :int = None):
    """Shows the target menu in the ASEAN Phonebook program.
    
    Args:
        target (str): Target menu to show. Refer to MENUS dictionary.
        inline (int): If not none, then will create an inline menu with n items each.
    """
    print("\n<-----Menu----->")
    i = 1 if inline != None else None # Start the item counter if inline is provided
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1
        
def receiveContactInfo() -> Contact:
    """Cast several prompts for user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based from data.
    """
    stdn = prompt("Enter student number: ")    
    lname = prompt("Enter surname: ")
    fname = prompt("Enter first name: ")
    occupation = prompt("Enter occupation: ")
    gender = prompt("Enter gender (M for male, F for female): ")
    cc = int(prompt("Enter country code: "))
    area = int(prompt("Enter area code: "))
    number = int(prompt("Enter number: "))
    return Contact(stdn,fname,lname,occupation,gender,cc,area,number)

def prompt(phrase: str) -> str:
    """Prompts an input to the user

    Args:
        phrase (str): Input phrase.

    Returns:
        str : Returns a string type of inputted value.
    """
    return input(phrase)

def convertChoices(choices: list) -> list:
    """Converts choices from the phonebook menu
    into proper country code value for accuracy purposes.

    Args:
        choices (list): Choices selected by user during prompt.

    Returns:
        list: Converted values of choices.
    """
    for i in range(0, len(choices)):
        match choices[i]:
            case 1:
                choices[i] = 856
            case 2:
                choices[i] = 855
            case 3:
                choices[i] = 66
            case 4: 
                choices[i] = 84
            case 5:
                choices[i] = 60
            case 6:
                choices[i] = 63
            case 7:
                choices[i] = 62
            case 8:
                choices[i] = 670
            case 9:
                choices[i] = 95
            case 10:
                choices[i] = 673
            case 11:
                choices[i] = 65
    return choices
                

if __name__ == "__main__":
    pb = ContactList()
    while True:
        showMenu("main")
        opt = int(input("Select Operation: "))
        # Complete your code here
        if opt == 1:
            while True:
                try:
                    stdn = int(input("Enter student number: "))
                except ValueError:
                    # If the input is not an integer, prompt again
                    print("Invalid input. Please enter a valid integer.")
                    continue

                lname = input("Enter surname: ")
                lname_invalid = False
                for i in lname:
                    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == ' ' or i == '\t'):
                        lname_invalid = True
                        break
                if lname_invalid:
                    print("Invalid input. Last name should not contain numbers.")
                    continue

                fname = input("Enter first name: ")
                fname_invalid = False
                for i in fname:
                    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == ' ' or i == '\t'):
                        fname_invalid = True
                        break
                if fname_invalid:
                    print("Invalid input. First name should not contain numbers.")
                    continue

                occupation = input("Enter occupation: ")
                occupation_invalid = False
                for i in occupation:
                    if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == ' ' or i == '\t'):
                        occupation_invalid = True
                        break
                if occupation_invalid:
                    print("Invalid input. Occupation should not contain numbers.")
                    continue

                gender = input("Enter gender (M for male, F for female): ")
                # Normalize gender input to uppercase
                if gender == 'f':
                    gender = 'F'
                elif gender == 'm':
                    gender = 'M'
                elif gender == 'M':
                    gender = 'M'
                elif gender == 'F':
                    gender = 'F'
                else:
                    print("Invalid input. There are only 2 genders.")
                    continue
                if gender.upper() not in {'M', 'F'}:
                    print("Invalid input. Please enter 'M' for male or 'F' for female.")
                    continue

                while True:
                    try:
                        # Ensure it is a valid ASEAN country code
                        cc = int(input("Enter country code: "))
                        if cc in [856, 855, 66, 84, 60, 63, 62, 670, 95, 673, 65]:
                            break 
                        else:
                            print("Invalid country code. Please enter a valid ASEAN country code.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for the country code.")

                try:
                    area = int(input("Enter area code: "))
                    number = int(input("Enter number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values for area code and number.")
                    continue

                # New Contact object with the provided information
                contact = Contact(stdn, fname, lname, occupation, gender, cc, area, number)
                pb.insert(contact)

                add_new_entry = input("Contact added successfully! Do you want to add a new entry? (yes/no): ").lower()
                while add_new_entry not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    add_new_entry = input("Do you want to add a new entry? (yes/no): ").lower()

                if add_new_entry == "yes":
                    print("Add a new Entry")
                elif add_new_entry == "no":
                    break  

        elif opt == 2:
            # Check if the phonebook is empty 
            if pb.size == 0:
                print("Phonebook is empty. Add a contact first.")
            else:
                while True:
                    showMenu("edit")
                    try:
                        edit_opt = int(input("Select Edit Operation: "))
                        if edit_opt not in range(1, 9):
                            print("Invalid option. Please select a number between 1 and 8.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                        continue

                    if edit_opt == 8:
                        print("Going back to the main menu.")
                        break

                    stdn = input("Enter student number to edit: ")

                    try:
                        stdn = int(stdn)
                    except ValueError:
                        print("Invalid input. Please enter a numeric student number.")
                        continue

                    contact = pb.getContact(stdn)

                    if contact is None:
                        print("DEBUG: Contact not found with student number {}".format(stdn))
                        print("DEBUG: Available contacts in the phonebook:")
                        for c in pb.phonebook:
                            print(c)
                        print("Contact not found. Returning to the main menu.")
                        break  

                    # Store the original values for comparison if their are changes
                    original_values = {
                        "student_number": contact.getStudentNumber(),
                        "last_name": contact.getLName(),
                        "gender": contact.getGender(),
                        "occupation": contact.getOccupation(),
                        "country_code": contact.getNumericCountryCode(),
                        "area_code": contact.getAreaCode(),
                        "contact_number": contact.getContactNumber()
                    }

                    # Edit operation based on user selection
                    if edit_opt == 1:
                        # Edit student number
                        new_stdn = input("Enter new student number: ")
                        contact.setStudentNumber(new_stdn)
                    
                    elif edit_opt == 2:
                        # Edit last name
                        new_lname = input("Enter new last name: ")
                        contact.setLName(new_lname)
                    
                    elif edit_opt == 3:
                        # Edit gender
                        new_gender = input("Enter new gender: ").capitalize()
                        if new_gender not in ["M", "F"]:
                            print("Sorry, that is an invalid value for gender.")
                            continue 
                        else:
                            contact.setGender(new_gender)
                    
                    elif edit_opt == 4:
                        # Edit occupation
                        new_occupation = input("Enter new occupation: ")
                        contact.setOccupation(new_occupation)
                    
                    elif edit_opt == 5:
                        # Edit country code
                        new_cc = input("Enter new country code: ")
                        try:
                            new_cc = int(new_cc)
                            contact.setCountryCode(new_cc)
                        except ValueError:
                            print("Invalid input. Please enter a numeric country code.")
                            continue
                    
                    elif edit_opt == 6:
                        # Edit area code
                        new_area = input("Enter new area code: ")
                        try:
                            new_area = int(new_area)
                            contact.setAreaCode(new_area)
                        except ValueError:
                            print("Invalid input. Please enter a numeric area code.")
                            continue
                    
                    elif edit_opt == 7:
                        # Edit contact number
                        new_number = input("Enter new number: ")
                        try:
                            new_number = int(new_number)
                            contact.setContactNumber(new_number)
                        except ValueError:
                            print("Invalid input. Please enter a numeric contact number.")
                            continue
                    else:
                        print("Invalid option.")

                    # Compare original values with the updated values
                    if original_values != {
                        "student_number": contact.getStudentNumber(),
                        "last_name": contact.getLName(),
                        "gender": contact.getGender(),
                        "occupation": contact.getOccupation(),
                        "country_code": contact.getNumericCountryCode(),
                        "area_code": contact.getAreaCode(),
                        "contact_number": contact.getContactNumber()
                    }:
                        # If changes were made
                        print("Edited contact:", contact)
                    else:
                        # If no changes were made
                        print("No changes were made!")

                    break
        
        elif opt == 3:
            # Check if the phonebook is empty
            if pb.size == 0:
                print("Phonebook is empty. Add a contact first.")
            else:
                stdn = input("Enter student number to delete: ")

                try:
                    stdn = int(stdn)
                except ValueError:
                    print("Invalid input. Please enter a numeric student number.")
                    continue  

                deleted_contact = pb.deleteContact(stdn)

                if deleted_contact:
                    print("Deleted contact:", deleted_contact)
                else:
                    print("Contact not found.")

        elif opt == 4:
            if pb.size == 0:
                print("Phonebook is empty. Add a contact first.")
            else:
                showMenu("views")
                view_opt = int(input("Select View Operation: "))
                if view_opt == 1:
                    selected_countries = set()  

                    while True:
                        print("From which country?:")
                        showMenu("cc", inline=3)
                        cc_opt = int(input("Enter choice (0 to exit): "))

                        if cc_opt == 0:
                            break  
                        elif 1 <= cc_opt <= 12:
                            selected_countries.add(cc_opt)  
                            converted_countries = convertChoices(list(selected_countries))  
                            filtered_contacts = [contact for contact in pb.phonebook if contact and contact.getNumericCountryCode() in converted_countries]

                            if not filtered_contacts:
                                print("No contacts found for the selected countries.")
                            else:
                        
                                filtered_contacts.sort(key=Contact.getLName)

                                print(f"\nHere are the students from the selected countries:\n")
                                for contact in filtered_contacts:
                                    print(contact)

                        else:
                            print("Invalid choice. Please try again.")
                    print("\nGoing back to the search menu.")


                
                elif view_opt == 2:
                    # Search by surname
                    surname = input("Enter surname to search: ")
                    matching_contacts = pb.getContactBySurname(surname)

                    if matching_contacts:
                        print("Contacts with the surname '{}':".format(surname))
                        for contact in matching_contacts:
                            print(contact)
                    else:
                        print("No contacts found with the surname '{}'.".format(surname))

                elif view_opt == 3:
                    # View all
                    print(pb)
                elif view_opt == 4:
                    # Go back to main menu
                    pass
                else:
                    print("Invalid option.")

        elif opt == 5:
            # Exit
            break
        else:
            print("Invalid option.")