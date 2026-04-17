import csv
import json
import os
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

    def edit_name(self, old_name: str, new_name: str) -> bool:
        """
        Rename a contact while preserving all phone numbers.
        :param old_name: Existing contact name
        :param new_name: New contact name
        :return: True if renamed, False if old contact does not exist
        """
        if old_name not in self.phonebook:
            return False

        numbers = self.phonebook.pop(old_name)
        if new_name in self.phonebook:
            self.phonebook[new_name].extend(numbers)
        else:
            self.phonebook[new_name] = numbers
        return True

    def edit_number(self, name: str, old_number: str, new_number: str) -> bool:
        """
        Replace one phone number for an existing contact.
        :param name: Contact name
        :param old_number: Existing number to replace
        :param new_number: New number to set
        :return: True if number was replaced, False otherwise
        """
        if name not in self.phonebook:
            return False

        try:
            index = self.phonebook[name].index(old_number)
        except ValueError:
            return False

        self.phonebook[name][index] = new_number
        return True

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
    print("5) Lookup all contact names")
    print("6) Edit contact name")
    print("7) Edit contact number")
    print("8) Save now")
    print("9) Import contacts from CSV")
    print("10) Exit")


def load_phonebook(file_path: str) -> Dict[str, List[str]]:
    """
    Load phonebook data from JSON file if it exists.
    :param file_path: Path to persisted phonebook file
    :return: Dictionary mapping names to phone number lists
    """
    if not os.path.exists(file_path):
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, dict):
            return {
                str(name): [str(number) for number in numbers]
                for name, numbers in data.items()
                if isinstance(numbers, list)
            }
    except (json.JSONDecodeError, OSError):
        pass

    return {}


def save_phonebook(file_path: str, phonebook: PhoneBook) -> None:
    """
    Save phonebook data to JSON file.
    :param file_path: Path to persisted phonebook file
    :param phonebook: PhoneBook instance to serialize
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(phonebook.get_map(), file, indent=2)


def import_phonebook_csv(file_path: str, phonebook: PhoneBook) -> Dict[str, int]:
    """
    Import contacts from CSV into an existing phonebook.
    Supports either:
    - first_name,last_name,phone_number
    - name,phone_number
    :param file_path: CSV file path to import
    :param phonebook: PhoneBook instance to modify
    :return: Dictionary with imported and skipped row counts
    """
    imported = 0
    skipped = 0

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name = (row.get("first_name") or "").strip()
            last_name = (row.get("last_name") or "").strip()
            full_name = " ".join(part for part in [first_name, last_name] if part)
            name = (row.get("name") or full_name).strip()
            phone_number = (row.get("phone_number") or "").strip()

            if not name or not phone_number:
                skipped += 1
                continue

            phonebook.add(name, phone_number)
            imported += 1

    return {"imported": imported, "skipped": skipped}


def run_menu() -> None:
    save_file_path = os.path.join(os.path.dirname(__file__), "saved_phonebook.json")
    phonebook = PhoneBook(load_phonebook(save_file_path))

    while True:
        print_menu()
        selection = input("Choose an option: ").strip()

        if selection == "1":
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            phonebook.add(name, phone_number)
            save_phonebook(save_file_path, phonebook)
            print(f"Added entry for {name} and saved.")
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
            save_phonebook(save_file_path, phonebook)
            print(f"Removed {name} if it existed, and saved.")
        elif selection == "5":
            names = phonebook.get_all_contact_names()
            if names:
                print(f"All contact names: {names}")
            else:
                print("PhoneBook is empty.")
        elif selection == "6":
            old_name = input("Enter current name: ").strip()
            new_name = input("Enter new name: ").strip()
            if phonebook.edit_name(old_name, new_name):
                save_phonebook(save_file_path, phonebook)
                print(f"Renamed {old_name} to {new_name}.")
            else:
                print(f"No contact found for {old_name}.")
        elif selection == "7":
            name = input("Enter name: ").strip()
            old_number = input("Enter current phone number: ").strip()
            new_number = input("Enter new phone number: ").strip()
            if phonebook.edit_number(name, old_number, new_number):
                save_phonebook(save_file_path, phonebook)
                print(f"Updated number for {name}.")
            else:
                print(f"Could not update number for {name}.")
        elif selection == "8":
            save_phonebook(save_file_path, phonebook)
            print("PhoneBook saved.")
        elif selection == "9":
            csv_path = input("Enter CSV file path: ").strip()
            if not csv_path:
                print("No file path entered.")
                continue

            try:
                result = import_phonebook_csv(csv_path, phonebook)
                save_phonebook(save_file_path, phonebook)
                print(
                    f"Imported {result['imported']} contacts from CSV. "
                    f"Skipped {result['skipped']} row(s)."
                )
            except FileNotFoundError:
                print("CSV file not found.")
            except OSError:
                print("Unable to read CSV file.")
        elif selection == "10":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-10.")


if __name__ == "__main__":
    run_menu()