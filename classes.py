class library:
    name_list=[]
    book_list=[]
    books=["basic of python","basic of dsa","basic of java ","basic of c++"]
    def registration(self):
        name=input("enter your name=")
        self.name_list.append(name)
        print( "registration is succesfull")

    def adding_new_books(self):
        book_name=input("enter your book name for add in library=")
        self.book_list.append(book_name)
        print("Adding book Succesfully!!!!")

    def borrowing_book(self):
        print(self.books)
        print("Available books:")
        for i in self.books:
              print(i)
        self.book_namee=input("select your book:")
        self.book_namee.lower()
        if self.book_namee in self.books:
            self.books.remove(self.book_namee)
            print("book borrowed succesfull")
        else:
            print("book is not avilable")
       
    def returning_book(self):
        self.returning_book_name=input("enetr your returning bopok name=")
        self.books.append(self.returning_book_name)
        print("returning book succesfulll")



obj=library()
print("Welcome to Library!!!!!")
print("please select your work....")


while(True):
    methods=["1. Registration","2.Adding new books","3.borrowing books","4.returning books","5.end"]
    for i in methods:
        print(i)
    number=int(input("enter your number for work="))
    if number==1:
            obj.registration()
    elif number==2:
            obj.adding_new_books()
    elif number==3:
            obj.borrowing_book()
    elif number==4:
            obj.returning_book()
    else:
            print("Thank you!!!")
            break .
lib.borrow("Basics of Python")
lib.return_book("Basics of Python")
lib.return_book("Basics of Java")





