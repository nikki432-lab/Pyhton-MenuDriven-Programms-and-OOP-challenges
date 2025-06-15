
import uuid
from datetime import date, timedelta

class Book:
    def __init__(self, title, author):
        self.book_id = str(uuid.uuid4())[:8]
        self.title = title
        self.author = author
        self.is_available = True

    def mark_borrowed(self):
        self.is_available = False

    def mark_returned(self):
        self.is_available = True

class User:
    def __init__(self, name):
        self.user_id = str(uuid.uuid4())[:8]
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book_id, due_date):
        self.borrowed_books[book_id] = due_date

    def return_book(self, book_id):
        return self.borrowed_books.pop(book_id, None)

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, title, author):
        book = Book(title, author)
        self.books[book.book_id] = book
        print(f"\n Book added:[{book.book_id}] {book.title} by {book.author}")

    def delete_book(self,book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_available:
                del self.books[book_id]
                print(f"\n Book [{book_id}] deleted.")
            else:
                print("\n Cannot delete: Book is currently borrowed.")
        else:
            print("\n Book ID not found")
    
    def register_user(self,name):
        user = User(name)
        self.users[user.user_id] = user
        print(f"\n User registered: [{user.user_id}] {user.name}")

    def borrow_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]
            if book.is_available:
                due_date = date.today() + timedelta(days=14)
                user.borrow_book(book_id, due_date)
                book.mark_borrowed()
                print(f"\n {book.title} borrowed. Due:{due_date}")
            else:
                print("\n Book not available.")
        else:
            print("\n Invalid user ID or book ID.")

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            due_date = user.return_book(book_id)
            if due_date:
                book = self.books[book_id]
                book.mark_returned()
                today = date.today()
                if today > due_date:
                    penalty  = (today-due_date).days * 2
                    print(f"\n Late return. penalty: ${penalty}")
                else:
                    print("\n Book returned on time")
            else:
                print("\n This book wasn't borrowed by that user.")
        else:
            print("\n Invalid user ID or book ID.")

    def view_availablebooks(self):
        print("\nAvailable Books: ")
        for book in self.books.values():
            if book.is_available:
                print(f"[{book.book_id}] {book.title} by {book.author}")

def main():
    library = Library()

    library.add_book("Fluent python", "Luciano Ramalho")
    library.add_book("Python Tricks", "dan Bader")
    library.register_user("Nikhil")
    library.register_user("Akhil")

    while True:
        print("\n------Library Menu-------")
        print("1. View Available Books")
        print("2. Borrow a book")
        print("3. Return a Book")
        print("4. Add a new book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Enter a Choice: ")

        if choice == '1':
            library.view_availablebooks()
        elif choice == '2':
            uid = input("User ID: ")
            bid = input("Book ID: ")
            library.borrow_book(uid, bid)
        elif choice == '3':
            uid = input("User ID: ")
            bid = input("Book ID: ")
            library.return_book(uid, bid)
        elif choice == '4':
            title = input("Book Title: ")
            author = input("Author: ")
            library.add_book(title, author)
        elif choice == '5':
            bid = input("Enter Book ID to delete: ")
            library.delete_book(bid)
        elif choice == '6':
            print("\nExiting the library system. Goodbye!")
            break
        else:
            print("\n Invalid chice.")

if __name__ == "__main__":
    main()
    



