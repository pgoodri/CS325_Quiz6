class BookCatalog:
    def add_book(self, book):
        # Add a book to the catalog
        print("Adding book to catalog...")

    def remove_book(self, book):
        # Remove a book from the catalog
        print("Removing book from catalog...")

class BookSearch:
    def search_books(self, query):
        # Search for books by title, author, or genre
        print("Searching for books...")

class BookLoan:
    def borrow_book(self, book_id, user_id):
        # Borrow a book for a registered user
        print("Borrowing book...")

    def return_book(self, book_id, user_id):
        # Return a book for a registered user
        print("Returning book...")

class ReportGenerator:
    def generate_reports(self):
        # Generate reports on borrowings, overdue books, and book popularity
        print("Generating reports...")

class Library(BookCatalog, BookSearch, BookLoan, ReportGenerator):
    def __init__(self):
        print("Library instance created")

def main():
    # Example usage
    library = Library()

    # Guest user actions
    guest_user = BookSearch()
    guest_user.search_books("Harry Potter")

    # Librarian actions
    librarian = Library()
    librarian.add_book("New Book")
    librarian.generate_reports()

if __name__ == "__main__":
    main()