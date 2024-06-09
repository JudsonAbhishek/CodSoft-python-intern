class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nWelcome to Contact Book!")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if search_results:
                print("Search Results:")
                for contact in search_results:
                    print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone_number = input("Enter new phone number (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
