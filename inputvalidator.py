def validate_positive_number(func):
    def wrapper(number):
        if number>0:
            func(number)
        else:
            print("error!!!,please enter the positive number")
    return wrapper


@validate_positive_number
def positive(number):
    print("positive number")

positive(18)
