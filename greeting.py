def greeting(name):
    print(f"Hello,{name}")





def area_rectangle(length,width):
    area = length*width
    return area

def is_even(number):
    if number % 2 ==0 :
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


number=int(input("Enter a number: "))
is_even(number)

print(area_rectangle(23,67))
greeting("Aminu!")