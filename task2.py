# розбиває введений рядок на слова, використовуючи пробіл як розділювач
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# новий контакт
def add_contact(username, phone, contacts):
    contacts[username.lower()] = phone  # записати низьким регістром
    return "Contact added."


# змінити контакт
def change_contact(username, phone, contacts):
    if username.lower() in contacts:
        contacts[username.lower()] = phone
        return "Contact updated."
    else:
        return "Contact not found."


# показати контакт
def show_phone(username, contacts):
    if username.lower() in contacts:
        return contacts[username.lower()]
    else:
        return "Contact not found."


# показати всі контакти
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join(
        [
            f"{name.capitalize()}: {phone}" for name, phone in contacts.items()
        ]  # контакти виводяться з великої літери
    )
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                username, phone = args
                print(add_contact(username, phone, contacts))
            else:
                print("Invalid command.")
        elif command == "change":
            if len(args) == 2:
                username, phone = args
                print(change_contact(username, phone, contacts))
            else:
                print("Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                username = args[0]
                result = show_phone(username, contacts)
                print(result)
            else:
                print("Invalid command.")
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
