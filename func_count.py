def call_count(func):
    count=0

    def wrapper():
        nonlocal count
        count+=1
        print(f"function calls {count} times")
        return func()
    return wrapper

@call_count
def say_hell():
    print("hello,AB")

say_hell()
