class Patron:
    def __init__(self,name):
        self.name = name


class Book:
    def __init__(self,bookname):
        self.bookname = bookname
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self,title):
        self.books.append(Book(title))
        print(title,"Added")

    def register_patron(self,name):
        self.patrons.append(Patron(name))

    def borrow(self,bookname):
        for book in self.books:
            if book.bookname == book.available:
                book.available = False
                print(bookname,"borrowed")
                return
                
            else:
               print("Book not available")
            
    def return_book(self,bookname):
        for book in self.books:
            if book.bookname ==bookname:
                book.available = True
                print(bookname,"returned")
                return
            else:
                print("book not found")


lib = Library()

lib.add_book("Basics of Python")
lib.add_book("Basics of Java")
lib.register_patron("AB")

lib.borrow("Basics of Python")
lib.return_book("Basics of Python")
lib.return_book("Basics of Java")





