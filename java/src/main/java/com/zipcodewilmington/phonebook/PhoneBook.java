package com.zipcodewilmington.phonebook;

import java.util.List;
import java.util.ArrayList;
//import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Created by leon on 1/23/18.
 * Made WAY better by kristofer 6/16/20
 */
public class PhoneBook {

    private final Map<String, List<String>> phonebook;

    public PhoneBook(Map<String, List<String>> map) {
        this.phonebook = null;
    }

    public PhoneBook() {
        this(null);
    }

    public void add(String name, String phoneNumber) {
    }

    public void addAll(String name, String... phoneNumbers) {
    }

    public void remove(String name) {
    }

    public Boolean hasEntry(String name) {
        return null;
    }

    public List<String> lookup(String name) {
        return null;
    }

    public String reverseLookup(String phoneNumber)  {
        return null;
    }

    public List<String> getAllContactNames() {
        return null;
    }

    public Map<String, List<String>> getMap() {
        return null;
    }

    public static void main(String[] args) {
        PhoneBook phoneBook = new PhoneBook();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            printMenu();
            String selection = scanner.nextLine().trim();

            switch (selection) {
                case "1":
                    handleAdd(phoneBook, scanner);
                    break;
                case "2":
                    handleLookup(phoneBook, scanner);
                    break;
                case "3":
                    handleReverseLookup(phoneBook, scanner);
                    break;
                case "4":
                    running = false;
                    System.out.println("Goodbye.");
                    break;
                default:
                    System.out.println("Invalid option. Please choose 1-4.");
            }
            System.out.println();
        }
    }

    private static void printMenu() {
        System.out.println("PhoneBook Menu");
        System.out.println("1) Add contact number");
        System.out.println("2) Lookup numbers by name");
        System.out.println("3) Reverse lookup by number");
        System.out.println("4) Exit");
        System.out.print("Choose an option: ");
    }

    private static void handleAdd(PhoneBook phoneBook, Scanner scanner) {
        System.out.print("Enter name: ");
        String name = scanner.nextLine().trim();
        System.out.print("Enter phone number: ");
        String phoneNumber = scanner.nextLine().trim();

        phoneBook.add(name, phoneNumber);
        System.out.println("Added entry for " + name + ".");
    }

    private static void handleLookup(PhoneBook phoneBook, Scanner scanner) {
        System.out.print("Enter name to lookup: ");
        String name = scanner.nextLine().trim();
        List<String> numbers = phoneBook.lookup(name);

        if (numbers == null || numbers.isEmpty()) {
            System.out.println("No numbers found for " + name + ".");
        } else {
            System.out.println("Numbers for " + name + ": " + numbers);
        }
    }

    private static void handleReverseLookup(PhoneBook phoneBook, Scanner scanner) {
        System.out.print("Enter number to reverse lookup: ");
        String phoneNumber = scanner.nextLine().trim();
        String name = phoneBook.reverseLookup(phoneNumber);

        if (name == null) {
            System.out.println("No contact found for " + phoneNumber + ".");
        } else {
            System.out.println(phoneNumber + " belongs to " + name + ".");
        }
    }
}
