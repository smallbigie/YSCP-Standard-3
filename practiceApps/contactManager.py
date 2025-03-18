# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        print(f"Contact for {name} already exists.")
    else:
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} added successfully.")

# Function to view all contacts
def view_all_contacts():
    if contacts:
        print("\n--- All Contacts ---")
        for name, details in contacts.items():
            print(f"{name}: Phone - {details['phone']}, Email - {details['email']}")
    else:
        print("No contacts found.")

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name of the contact to search for: ")
    if name in contacts:
        details = contacts[name]
        print(f"Contact found: {name}: Phone - {details['phone']}, Email - {details['email']}")
    else:
        print(f"Contact for {name} not found.")

# Function to remove a contact
def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} removed successfully.")
    else:
        print(f"Contact for {name} not found.")

# Function to update a contact's information
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter the new phone number for {name}: ")
        email = input(f"Enter the new email for {name}: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} updated successfully.")
    else:
        print(f"Contact for {name} not found.")

# Main function to run the menu-driven system
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Remove a Contact")
        print("5. Update a Contact")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
