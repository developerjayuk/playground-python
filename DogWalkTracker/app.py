from database import add_entry, get_entries

menu = """Please choose one of the following options:
1. Add a new dog diary entry
2. View all dog diary entries
3. Exit

Your choice: """
welcome = "Welcome to the Dog Walk Tracker App!"


def prompt_new_entry():
    entry_content = input("How many walks did you go on today? ")
    entry_date = input("What date is this entry for? (DD-MM-YYYY) ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"Date: {entry['date']}, Content: {entry['content']}\n\n")


while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())

    else:
        print("Invalid choice. Please try again.")
