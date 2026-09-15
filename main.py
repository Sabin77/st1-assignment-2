# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

##Functions in Python
# def welcome_screen() -> None:
#     print("Welcone to ST1")
#     print("__" *15)
#
# welcome_screen()


#scope: global, local, parameter, field
#return type


# def add_numbers(number1: float = 0, number2: float= 0) -> float|int:
#     return number1 + number2
#
# print(add_numbers(1, 2))
# print(add_numbers(number2= 5, number1=2))
#
# def add_numbers(*number1) -> float|int:
#     return sum(number1)
#
# print(add_numbers(1, 2, 3, 5))
def factorial(number: int):
    if number == 0:
        return 1
    print(f"{number} * {number-1}")
    return  number * factorial(number-1)

def main():
    factorial(5)

if __name__ == '__main__':
    main()


#
