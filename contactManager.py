# Global dictionary to store contacts
directory = {}

# Function to add a new contact
def create_contact():
    person = input("Enter the contact's name: ")
    if person in directory:
        print(f"{person} is already in the directory.")
    else:
        phone_number = input("Enter phone number: ")
        email_address = input("Enter email: ")
        directory[person] = {"phone": phone_number, "email": email_address}
        print(f"Contact for {person} successfully added.")


# Function to view all contacts
def list_contacts():
    if directory:
        print("\n--- Contact List ---")
        for person, info in directory.items():
            print(f"{person}: Phone - {info['phone']}, Email - {info['email']}")
    else:
        print("No contacts available.")


# Function to search for a contact by name
def find_contact():
    person = input("Enter the contact's name to search: ")
    if person in directory:
        info = directory[person]
        print(f"Found: {person} - Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"No contact found for {person}.")


# Function to remove a contact
def delete_contact():
    person = input("Enter the name of the contact to delete: ")
    if person in directory:
        del directory[person]
        print(f"{person}'s contact removed successfully.")
    else:
        print(f"No contact found for {person}.")


# Function to update a contact's information
def modify_contact():
    person = input("Enter the name of the contact to modify: ")
    if person in directory:
        new_phone = input(f"Enter the updated phone number for {person}: ")
        new_email = input(f"Enter the updated email for {person}: ")
        directory[person] = {"phone": new_phone, "email": new_email}
        print(f"Contact for {person} successfully updated.")
    else:
        print(f"No contact found for {person}.")


# Main function to run the menu-driven system
def run_contact_manager():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Remove a Contact")
        print("5. Update Contact Information")
        print("6. Exit")
       
        option = input("Select an option (1-6): ")
       
        if option == '1':
            create_contact()
        elif option == '2':
            list_contacts()
        elif option == '3':
            find_contact()
        elif option == '4':
            delete_contact()
        elif option == '5':
            modify_contact()
        elif option == '6':
            print("Closing Contact Manager. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    run_contact_manager()
