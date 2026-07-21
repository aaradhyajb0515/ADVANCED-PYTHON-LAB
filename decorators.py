#login decorator
def logger(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper

@logger
def display():
    print("welcome Student")

display()

#authentication decorator
logged_in=True
def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("please login first")
    return wrapper

@login_required
def profile():
    print("welcome to youe profile")

profile()

#execution time decorator
import time
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("Execution time=",end,start)
    return wrapper

@timer
def numbers():
    for i in range(1000000):
        pass

numbers()
#age validation
def validate_age(func):
    def wrapper(age):
        if age>=18:
            func(age)
        else:
            print("not eligible")
    return wrapper


@validate_age
def vote(age):
    print("eligible vote")

vote(18)
vote(15)
#exception handle
def exception(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print("error:",e)
    return wrapper
@exception
def division():
    print(10/0)

division()

#admin
user_role="admin"
def admin(func):
    def wrapper():
        if user_role=="admin":
            func()
        else:
            print("accceesed denied")
    return wrapper

@admin
def delete_record():
    print("record deleted")


delete_record()
