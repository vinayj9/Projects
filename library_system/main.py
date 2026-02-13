from lib_sys import Library
from lib_sys import Book
from lib_sys import Member

def confirm_action(message="Are you sure? (y/n): "):
    choice = input(message).strip().lower()
    return choice == "y"

def main():
    library = Library()   # Create one library instance
    library.load_from_file()
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display All Books")
        print("7. Display Borrowed Books")
        print("8. Check Overdue Books")
        print("9. Show Statistics")
        print("10. Add Member")
        print("11. Remove Member")
        print("12. Search Member")
        print("13. Exit")


        choice = input("Enter your choice (1-13): ").strip()

        if choice == "1":
            print("\n--- Add Book ---")
            
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()

            if not title or not author:
                print("Error: Title and author cannot be empty.")
                continue
            if not library.is_valid_isbn(isbn):
                print("Error: Invalid ISBN format. Must be 10 or 13 digits (hyphens allowed).")
                continue
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == "2":
            print("\n--- Remove Book ---")

            isbn = input("Enter ISBN of the book to remove: ").strip()

            if not isbn:
                print("Error: ISBN cannot be empty.Please enter a valid ISBN.")
                continue

            book = library.search_by_isbn(isbn)

            if not book:
                print("Error: No book found with that ISBN.")
                continue

            print(f"You are about to remove: {book.title}")

            if confirm_action():
                library.remove_book(isbn)
            else:
                print("Action cancelled.Returning to main menu.")

        elif choice == "3":
            print("\n--- Search Menu ---")
            print("1. Search by Title")
            print("2. Search by Author")
            print("3. Search by ISBN")

            sub_choice = input("Enter your choice (1-2-3): ").strip()

            if sub_choice not in ("1", "2", "3"):
                print("Invalid search option.")
                continue
            
            if sub_choice == "3":
                isbn = input("Enter ISBN: ").strip()

                if not isbn:
                    print("ISBN cannot be empty.")
                    continue

                book = library.search_by_isbn(isbn)

                if book:
                    print("\nBook Found:")
                    print(book)
                else:
                    print("No book found with that ISBN.")

                continue  # Skip list-style display logic
            
            search_term = input("Enter search term: ").strip()

            if not search_term:
                print("Search term cannot be empty.")
                continue

            if sub_choice == "1":
                results = library.search_by_title(search_term)
            else:
                results = library.search_by_author(search_term)
            
            # Display Results
            if results:
                print("\nSearch Results:")
                for index, book in enumerate(results, start=1):
                    print(f"{index}. {book}")
            else:
                print("No books found.")

        elif choice == "4":
            print("\n--- Borrow Book ---")

            isbn = input("Enter ISBN of the book: ").strip()
            if not isbn:
                print("Error: ISBN cannot be empty.")
                continue

            member_id = input("Enter Member ID: ").strip()
            if not member_id:
                print("Error: Member ID cannot be empty.")
                continue

            days_input = input("Enter number of days (press Enter for default 14): ").strip()

            if days_input == "":
                days = 14
            else:
                if not days_input.isdigit():
                    print("Error: Days must be a positive number.")
                    continue
                days = int(days_input)

                if days <= 0:
                    print("Error: Days must be greater than zero.")
                    continue

            library.borrow_book(isbn, member_id, days)

        elif choice == "5":
            print("\n--- Return Book ---")

            isbn = input("Enter ISBN of the book to return: ").strip()

            if not isbn:
                print("Error: ISBN cannot be empty.")
                continue

            library.return_book(isbn)

        elif choice == "6":
            library.display_all_books()

        elif choice == "7":
            library.display_borrowed_books()

        elif choice == "8":
            library.check_overdue()

        elif choice == "13":
            library.save_to_file()
            print("Library saved. Exiting program. Goodbye!")
            break
        elif choice =="9":
            library.show_statistics()
        elif choice =="10":
            print("\n--- Add Member ---")

            member_id = input("Enter Member ID: ").strip()
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()

            if not member_id or not name or not email:
                print("All fields are required.")
                continue

            member = Member(member_id, name, email)
            library.add_member(member)
            library.save_to_file()

        elif choice == "11":
            print("\n--- Remove Member ---")

            member_id = input("Enter Member ID to remove: ").strip()

            if not member_id:
                print("Member ID cannot be empty.")
                continue

            member = library.search_member(member_id)

            if not member:
                print("No member found.")
                continue

            print(f"You are about to remove member: {member.name}")

            if confirm_action():
                library.remove_member(member_id)
                library.save_to_file()
            else:
                print("Action cancelled.")

        elif choice == "12":
            print("\n--- Search Member ---")

            member_id = input("Enter Member ID: ").strip()

            if not member_id:
                print("Member ID cannot be empty.")
                continue

            member = library.search_member(member_id)

            if member:
                print("\nMember Found:")
                print(member)
                print("Borrowed Books:", member.borrowed_books)
            else:
                print("No member found with that ID.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
   
