from datetime import date, timedelta, datetime
import json

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.borrower_name = None
        self.due_date = None
        self.borrow_count = 0
    
    @property
    def is_borrowed(self):
        return self.borrower_name is not None
    
    def __str__(self):
        if self.is_borrowed:
            return (f"{self.title} by {self.author} "
                    f"| ISBN: {self.isbn} | "
                    f"Borrowed by {self.borrower_name}, Due: {self.due_date}")
        else:
            return (f"{self.title} by {self.author} "
                    f"| ISBN: {self.isbn} | Available")
    
    def __repr__(self):
        return (
            f"Book(title={self.title!r}, "
            f"author={self.author!r}, "
            f"isbn={self.isbn!r}, "
            f"borrowed={self.is_borrowed}, "
            f"borrower={self.borrower_name!r}, "
            f"due_date={self.due_date!r}, "
            f"borrow_count={self.borrow_count})"
        )
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "borrower_name": self.borrower_name,
            "due_date": self.due_date.strftime("%Y-%m-%d") if self.due_date else None,
            "borrow_count": self.borrow_count
        }
    
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["title"],
            data["author"],
            data["isbn"]
        )

        # Restore borrow-related fields
        book.borrower_name = data.get("borrower_name")
        book.borrow_count = data.get("borrow_count", 0)

        due_date_str = data.get("due_date")

        if due_date_str:
            book.due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        else:
            book.due_date = None

        return book
    

class Library:
    def __init__(self):
        self.books={}
        self.members = {}
        self.filename = "library_data.json"

# ADDING BOOKS
    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Error: A book with ISBN {book.isbn} already exists.")
            return False

        self.books[book.isbn] = book
        print(f'"{book.title}" added to the library.')
        self.save_to_file()
        return True   # Indicate success

# REMOVING BOOKS
    def remove_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            print(f"Error: No book found with ISBN {isbn}.")
            return
        if book.is_borrowed:
            print(f"Error: Cannot remove '{book.title}' because it is currently borrowed.")
            return
        del self.books[isbn]
        print(f"Success: '{book.title}' has been removed.")
        self.save_to_file()

# BORROWING BOOKS
    def borrow_book(self, isbn, member_id, days=14):
        book = self.books.get(isbn)
        member = self.members.get(member_id)
        if not book:
            print(f"Error: No book found with ISBN {isbn}.")
            return
        if not member:
            print(f"No member found with ID '{member_id}'.")
            return False
        # Check if already borrowed
        if book.is_borrowed:
            print(f"Error: '{book.title}' is already borrowed.")
            return
        #  Borrowing limit check
        if len(member.borrowed_books) >= 3:
            print(f"Member '{member.name}' has reached the borrowing limit (3 books).")
            return False
        
        # Set borrowing details
        book.borrower_name = member.name
        book.due_date = date.today() + timedelta(days=days)
        book.borrow_count += 1

        print(f"Success: '{book.title}' borrowed by {member.name}.")
        print(f"Due date: {book.due_date.strftime('%d-%m-%Y')}")
        member.borrowed_books.append(isbn)
        self.save_to_file()

# RETURNING BOOKS
    def return_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            print(f"Error: No book found with ISBN {isbn}.")
            return
        
        # Check if book is actually borrowed
        if not book.is_borrowed:
            print(f"Error: '{book.title}' is not currently borrowed.")
            return
        # Find member
        for member in self.members.values():
            if isbn in member.borrowed_books:
                member.borrowed_books.remove(isbn)
                break
        # Clear borrowing state
        book.borrower_name = None
        book.due_date = None

        print(f"Success: '{book.title}' has been returned.")
        self.save_to_file()
# ------------------------------------------------- #
    def search_by_title(self, search_term):
        search_term = search_term.lower()
        return [
        book for book in self.books.values()
        if search_term in book.title.lower()
        ]
    
    def search_by_author(self, search_term):
        search_term = search_term.lower()
        return [
        book for book in self.books.values()
        if search_term in book.author.lower()
        ]
    
    def display_all_books(self):
        if not self.books:
            print("No books added yet.")
            return
        for index, book in enumerate(self.books.values(), start=1):
            print(f"{index}. {book}")
    
    def display_borrowed_books(self):
        borrowed_books = [book for book in self.books.values() if book.is_borrowed]
        if not borrowed_books:
            print("No books are currently borrowed.")
            return

        print("Borrowed Books:")
        for index, book in enumerate(borrowed_books, start=1):
            print(f"{index}. {book.title} | "
                f"Borrowed by: {book.borrower_name} | "
                f"Due: {book.due_date.strftime("%d-%m-%Y")}")

    def check_overdue(self):
        today = date.today()
        overdue_books = []

        for book in self.books.values():
            if book.is_borrowed and book.due_date < today:
                days_overdue = (today - book.due_date).days
                overdue_books.append((book, days_overdue))

        if not overdue_books:
            print("No overdue books.")
            return

        print("Overdue Books:")
        for index, (book, days) in enumerate(overdue_books, start=1):
            print(f"{index}. {book.title} | "
                f"Borrowed by: {book.borrower_name} | "
                f"Due: {book.due_date.strftime('%d-%m-%Y')} | "
                f"{days} day(s) overdue")

    @staticmethod
    def is_valid_isbn(isbn):
        if not isbn:
            return False

        # Remove hyphens
        cleaned = isbn.replace("-", "")

        # Must be only digits after cleaning
        if not cleaned.isdigit():
            return False

        # Must be 10 or 13 digits
        return len(cleaned) in (10, 13)

    def search_by_isbn(self, isbn):
        return self.books.get(isbn)
    
    def show_statistics(self):
        total_books = len(self.books)
        borrowed_books = sum(1 for book in self.books.values() if book.is_borrowed)
        available_books = total_books - borrowed_books

        print("\n--- Library Statistics ---")
        print(f"Total Books: {total_books}")
        print(f"Available Books: {available_books}")
        print(f"Borrowed Books: {borrowed_books}")

        if total_books == 0:
            print("No books in library.")
            return

        # Find most borrowed book
        most_borrowed = max(self.books.values(), key=lambda b: b.borrow_count)

        if most_borrowed.borrow_count > 0:
            print(f"Most Borrowed Book: {most_borrowed.title} "
                f"({most_borrowed.borrow_count} times)")
        else:
            print("No books have been borrowed yet.")
    
    def save_to_file(self, filename=None):
        if filename is None:
            filename = self.filename
        try:
            with open(filename, "w") as file:
                data = {"books":[book.to_dict() for book in self.books.values()],
                "members": [member.to_dict() for member in self.members.values()]
                }
                json.dump(data, file, indent=4)

            # print(f"Library saved successfully to '{filename}'.")
        except Exception as e:
            print(f"Failed to save library: {e}")

    def load_from_file(self, filename="library_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            # Clear current books (optional but recommended)
            self.books.clear()
            self.members.clear()

            # Load books
            for book_dict in data.get("books", []):
                book = Book.from_dict(book_dict)
                self.books[book.isbn] = book

            # Load members
            for member_dict in data.get("members", []):
                member = Member.from_dict(member_dict)
                self.members[member.member_id] = member

            print(f"Library loaded successfully from '{filename}'.")

        except FileNotFoundError:
            print(f"No existing library file found ('{filename}'). Starting fresh.")

        except json.JSONDecodeError:
            print(f"Error: '{filename}' contains invalid JSON.")

        except Exception as e:
            print(f"Unexpected error while loading library: {e}")

    def add_member(self, member):
        if member.member_id in self.members:
            print(f"Member with ID '{member.member_id}' already exists.")
            return False

        self.members[member.member_id] = member
        print(f"Member '{member.name}' added successfully.")
        return True

    def remove_member(self, member_id):
        member = self.members.get(member_id)

        if not member:
            print(f"No member found with ID '{member_id}'.")
            return False

        if member.borrowed_books:
            print(f"Cannot remove member '{member.name}' because they have borrowed books.")
            return False

        del self.members[member_id]
        print(f"Member '{member.name}' removed successfully.")
        return True

    def search_member(self, member_id):
        return self.members.get(member_id)

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # list of ISBNs

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}, Email: {self.email})"

    def __repr__(self):
        return (
            f"Member(member_id={self.member_id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"borrowed_books={self.borrowed_books!r})"
        )

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["member_id"],
            data["name"],
            data["email"]
        )

        member.borrowed_books = data.get("borrowed_books", [])
        return member

