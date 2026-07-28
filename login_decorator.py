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
    print("welcome to your profile")

profile()
