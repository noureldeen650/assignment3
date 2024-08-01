Q1:


def even_check():
    number = input("Enter your number: ")
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            print("the number is even")
        else:
            print("the number is odd")
    else:
        print("invalid number please enter again")
        even_check()


even_check()
Q2:


def CtoF():
    global ctemp


ctemp = input("Enter degree number: ")
if ctemp.isdigit():
    ctemp = float(ctemp)
    ctemp = (ctemp * 9) / 5 + 32
else:
    print("invalid number please enter again")
    CtoF()
CtoF()
print(f"the temperature in fahreheit is : {ctemp}")
Q3:


def triangle_area():
    global area, base, height

    base = input("Enter base number: ")
    height = input("enter height: ")
    if base.isdigit() and height.isdigit():
        base = float(base)
        height = float(height)
    else:
        print("invalid number please enter again")
        triangle_area()
    area = (1 / 2) * base * height


triangle_area()
print(f"the area is : {area}")
Q4:


def average():
    print('enter the first number: ')
    number1 = input()
    if number1.isdigit():
        number1 = int(number1)

    else:
        print("enter a valid number")
        average()
    print("enter the second number: ")
    number2 = input()
    if number2.isdigit():
        number2 = int(number2)
    else:
        print("enter a valid number")
        average()

    print("enter the third number: ")
    number3 = input()

    if number3.isdigit():
        number3 = int(number3)
        avg = (number1 + number2 + number3) / 3
    else:
        print("enter a valid number")
        average()
    print(f"the average of the three numbers:{avg}")


average()

Q5:


def product():
    print('enter the first number: ')
    number1 = input()
    if number1.isdigit():
        number1 = int(number1)

    else:
        print("enter a valid number")
        product()
    print("enter the second number: ")
    number2 = input()
    if number2.isdigit():
        number2 = int(number2)
    else:
        print("enter a valid number")
        product()

    print("enter the third number: ")
    number3 = input()

    if number3.isdigit():
        number3 = int(number3)
        product = (number1 * number2 * number3)
    else:
        print("enter a valid number")
        product()
    print(f"the average of the three numbers:{product}")


product()
Q6:


def area_circumference():
    print('enter radius number: ')
    radius = input()
    if radius.isdigit():
        radius = float(radius)
        area = 3.14 * (radius) ** 2
        circumference = 2 * 3.14 * radius
        print(f"the area is: {area}")
        print(f"the circumference is: {circumference}")
    else:
        print("invalid number please enter again")
        area_circumference()


area_circumference()
Q7:


def multipleof5():
    print('enter the number: ')
    number = input()
    if number.isdigit():
        number = int(number)
        if number % 5 == 0:
            print("the number is a multiple of 5")
        else:
            print("the number is not a multiple of 5")
    else:
        print("invalid number please enter again")
        multipleof5()


multipleof5()
Q8:
for number in range(10, 51):
    if number % 3 == 0:
        print(number)
Q9:
Q10:


def factorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)


def input1():
    global number
    number = input("Enter a number : ")
    if number.isdigit():
        number = int(number)

    else:
        print("please enter a valid number")
        input1()
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")


input1()
Q11:


def swap(numbers, first, second):
    x = numbers[first]
    numbers[first] = numbers[second]
    numbers[second] = x


def input1():
    numbers = [10, 20, 30, 40, 50]
    number1 = input("enter the first index: ")

    if number1.isdigit():
        number1 = int(number1)
    else:
        print("enter a valid number")
        input1()

    number2 = input("enter the second index: ")
    if number2.isdigit():
        number2 = int(number2)
    else:
        print("enter a valid number")
        input1()
    swap(numbers, number1, number2)
    print("List after swapping:", numbers)


input1()
Q12:


def is_palindrome(s):
    reversed_string = ''

    for char in s:
        reversed_string = char + reversed_string

    if s == reversed_string:
        return True
    else:
        return False


def input1():
    string = input("Enter a string to check if it is a palindrome: ")

    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome')


input1()

