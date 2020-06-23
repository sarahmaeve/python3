def square(number):
    return number * number


try:
    input_number = input("What is your number: ")
    my_square = square(int(input_number))
    print(my_square)
except ValueError:
    print("Incorrect number type")

# if __name__ == "__main__":
#     input_number = input("What is your number: ")
#     print(square(int(input_number)))

