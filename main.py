class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False

    def __str__(self):
        return f"{self.isbn} - {self.title} by {self.author} ({self.publication_year})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publication_year):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = Book(isbn, title, author, publication_year)
            print(f"Book '{title}' added successfully.")

    def borrow_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"Book '{book.title}' is already borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
            else:
                print(f"Book '{book.title}' was not borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def view_available_books(self):
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")


library = Library()


library.add_book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.add_book("978-1-56619-909-4", "To Kill a Mockingbird", "Harper Lee", 1960)
library.add_book("978-0-7432-7356-5", "1984", "George Orwell", 1949)


library.borrow_book("978-3-16-148410-0")


library.borrow_book("978-3-16-148410-0")


library.view_available_books()


library.return_book("978-3-16-148410-0")


library.view_available_books()
