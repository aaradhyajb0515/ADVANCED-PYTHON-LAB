#Function Call Logger

from datetime import datetime
def timer(func):
    def wrapper():
        print("function called at:",datetime.now())
        return func()
    return wrapper

@timer
def time():
    print("hello,user")

time()
