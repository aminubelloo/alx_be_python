count = 10 #global variable

def outer_function():
    count = 5 #local variable within outer function

    def inner_function(): #inner function within outer function
        count = 2 #local variable within inner function
        print(f"Inner function: {count}")