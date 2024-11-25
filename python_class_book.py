class Book:
    def __init__(self, title, author, publication_year, pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages

    def book_info(self):
        return (f"Title: {self.title}, Author: {self.author}, "
                f"Year: {self.publication_year}, Pages: {self.pages}")

class EBook(Book):
    def __init__(self, title, author, publication_year, pages, file_type):
        super().__init__(title, author, publication_year, pages)
        self.file_type = file_type

    def ebook_info(self):
        return f"{self.book_info()}, File Type: {self.file_type}"

    def number_of_pages(self):
        return f"The number of pages in the book is {self.pages}."

def get_book_from_user():
    print("Enter book details:")
    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(input("Publication Year: "))
    pages = int(input("Number of Pages: "))
    is_ebook = input("Is it an eBook? (yes/no): ").strip().lower()

    if is_ebook == "yes":
        file_type = input("File Type (e.g., PDF, EPUB): ")
        book = EBook(title, author, publication_year, pages, file_type)
        print("\nEBook Information:")
        print(book.ebook_info())
        print(book.number_of_pages())
    else:
        book = Book(title, author, publication_year, pages)
        print("\nBook Information:")
        print(book.book_info())

get_book_from_user()