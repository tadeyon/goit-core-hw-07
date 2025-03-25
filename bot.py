from AddressBook import AddressBook
from Record import Record
from datetime import datetime

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."

    return inner       

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    try:
        record.add_birthday(birthday)
        return "Contact updated."
    except ValueError as e:
        return str(e)


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)

    if record is None:
        return "Contact not found."
    
    return datetime.strftime(record.birthday.value, '%d.%m.%Y')

@input_error
def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."
        
    return upcoming


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args

    if name not in book:
        raise KeyError

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact phone number has been changed."

@input_error
def get_phone(args, book: AddressBook):
    name = args[0]
    phones = book.find(name).phones
    for i in range(len(phones)):
        print(phones[i].value)

@input_error
def get_all(book: AddressBook):
    return "\n".join(f"{name} : {phone}" for name, phone in book.items()) or "No contacts found."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            get_phone(args, book)
        elif command == "all":
            print(get_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()