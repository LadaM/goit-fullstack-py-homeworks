from solid import LibraryManager, SearchableLibrary
import logging

def main():
    library = SearchableLibrary()
    library_manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, find, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library_manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library_manager.remove_book(title)
        elif command == "show":
            library_manager.show_books()
        elif command == "find":
            title = input("Enter book title to find: ").strip()
            library_manager.find_book(title)
        elif command == "exit":
            break
        else:
            logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
