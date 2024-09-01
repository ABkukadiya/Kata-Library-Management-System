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

    def add_book(self):
        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        publication_year = input("Enter Publication Year: ")

        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = Book(isbn, title, author, publication_year)
            print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        isbn = input("Enter ISBN of the book to borrow: ")
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"Book '{book.title}' is already borrowed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def return_book(self):
        isbn = input("Enter ISBN of the book to return: ")
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
            print("\nAvailable books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.borrow_book()
        elif choice == '3':
            library.return_book()
        elif choice == '4':
            library.view_available_books()
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
