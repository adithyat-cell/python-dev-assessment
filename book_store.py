# Task 2.2: OOP - Book Class

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        # Hardcoded current year as per assignment
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
if __name__ == "__main__":
    # Create two book objects
    book1 = Book("1984", "George Orwell", "1234567890", 1949)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", "0987654321", 1937)

    # Print details for each book
    for book in [book1, book2]:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Age: {book.get_age()} years")
        print(f"Summary: {book.get_summary()}")
        print("-" * 40)
