from typing import Dict, List, Optional


class PhoneBook:
    """
    Created by leon on 1/23/18.
    Made WAY better by kristofer 6/16/20
    Python version for beginner coders
    """

    def __init__(self, phonebook_dict: Optional[Dict[str, List[str]]] = None):
        """
        Constructor for PhoneBook
        :param phonebook_dict: Optional dictionary to initialize the phonebook with
        """
        self.phonebook = phonebook_dict if phonebook_dict is not None else {}

    def add(self, name: str, phone_number: str) -> None:
        """
        Add a phone number for a contact
        :param name: Contact name
        :param phone_number: Phone number to add
        """
        if name not in self.phonebook:
            self.phonebook[name] = []
        self.phonebook[name].append(phone_number)

    def add_all(self, name: str, *phone_numbers: str) -> None:
        """
        Add multiple phone numbers for a contact
        :param name: Contact name
        :param phone_numbers: Variable number of phone numbers to add
        """
        if name not in self.phonebook:
            self.phonebook[name] = []
        self.phonebook[name].extend(phone_numbers)

    def remove(self, name: str) -> None:
        """
        Remove a contact from the phonebook
        :param name: Contact name to remove
        """
        if name in self.phonebook:
            del self.phonebook[name]

    def has_entry(self, name: str, phone_number: str = None) -> bool:
        """
        Check if a contact exists, optionally with a specific phone number
        :param name: Contact name to check
        :param phone_number: Optional phone number to check
        :return: True if contact exists (with phone number if specified), False otherwise
        """
        if name not in self.phonebook:
            return False
        if phone_number is None:
            return True
        return phone_number in self.phonebook[name]

    def lookup(self, name: str) -> List[str]:
        """
        Look up all phone numbers for a contact
        :param name: Contact name to look up
        :return: List of phone numbers for the contact
        """
        return self.phonebook.get(name, [])

    def reverse_lookup(self, phone_number: str) -> str:
        """
        Find the contact name for a given phone number
        :param phone_number: Phone number to look up
        :return: Contact name associated with the phone number
        """
        for name, phone_numbers in self.phonebook.items():
            if phone_number in phone_numbers:
                return name
        return None

    def reverseLookup(self, phone_number: str) -> str:
        """CamelCase alias to match the Java-style method name used in the prompt."""
        return self.reverse_lookup(phone_number)

    def get_all_contact_names(self) -> List[str]:
        """
        Get all contact names in the phonebook
        :return: List of all contact names
        """
        return list(self.phonebook.keys())

    def get_map(self) -> Dict[str, List[str]]:
        """
        Get the underlying dictionary representation of the phonebook
        :return: Dictionary mapping names to lists of phone numbers
        """
        return self.phonebook


def print_menu() -> None:
    print("\nPhoneBook Menu")
    print("1) Add contact number")
    print("2) Lookup numbers by name")
    print("3) Reverse lookup by number")
    print("4) Remove contact by name")
    print("5) Exit")


def run_menu() -> None:
    phonebook = PhoneBook()

    while True:
        print_menu()
        selection = input("Choose an option: ").strip()

        if selection == "1":
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            phonebook.add(name, phone_number)
            print(f"Added entry for {name}.")
        elif selection == "2":
            name = input("Enter name to lookup: ").strip()
            numbers = phonebook.lookup(name)
            if numbers:
                print(f"Numbers for {name}: {numbers}")
            else:
                print(f"No numbers found for {name}.")
        elif selection == "3":
            phone_number = input("Enter number to reverse lookup: ").strip()
            name = phonebook.reverseLookup(phone_number)
            if name is None:
                print(f"No contact found for {phone_number}.")
            else:
                print(f"{phone_number} belongs to {name}.")
        elif selection == "4":
            name = input("Enter name to remove: ").strip()
            phonebook.remove(name)
            print(f"Removed {name} if it existed.")
        elif selection == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    run_menu()