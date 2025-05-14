class Book:
    total_books = 0  # Class variable shared by all instances

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Automatically increment when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("Pride and Prejudice", "Jane Austen")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Print total number of books
print("Total books:", Book.total_books)

