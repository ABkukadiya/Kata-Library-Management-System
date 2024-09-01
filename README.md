# Library Management System

## Overview
This Library Management System is a simple Python implementation that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. The system is designed to be easy to use and understand, making it suitable for small libraries or as a starting point for more complex systems.

## Features

### 1. Book Management
- Each book in the system is represented by a `Book` class, which includes attributes such as:
  - ISBN (International Standard Book Number)
  - Title
  - Author
  - Publication Year
  - Availability Status

### 2. Library Operations
The `Library` class provides the following functionalities:

#### Adding Books
- Users can add new books to the library.
- Each book must have a unique ISBN.
- If a book with the same ISBN already exists, the system will raise an error.

#### Borrowing Books
- Users can borrow available books from the library.
- The system checks if the requested book exists and is available.
- If the book is not available or doesn't exist, an appropriate error is raised.
- When a book is borrowed, its availability status is updated.

#### Returning Books
- Users can return previously borrowed books.
- The system verifies that the book exists and was actually borrowed.
- Upon return, the book's availability status is updated.

#### Viewing Available Books
- Users can view a list of all currently available books in the library.
- If no books are available, the system informs the user.

## How It Works

1. The system initializes an empty library.
2. Books can be added to the library using their ISBN, title, author, and publication year.
3. When a user attempts to borrow a book, the system checks its availability and updates the status if possible.
4. When a book is returned, the system verifies the return and updates the book's status.
5. Users can request a list of all available books at any time.

## Error Handling
The system includes error handling to manage common issues:
- Attempting to add a book with an existing ISBN
- Trying to borrow a non-existent or unavailable book
- Attempting to return a book that wasn't borrowed

## Extensibility
This system provides a foundation that can be easily extended to include more features such as:
- User management
- Due date tracking
- Book reservations
- More detailed book information

By using object-oriented principles, the code remains organized and can be expanded upon as needed.

## Usage
To use this Library Management System, simply import the `Library` class and create an instance of it. You can then use the provided methods to manage your library.

## Contributing
Contributions to improve the Library Management System are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

