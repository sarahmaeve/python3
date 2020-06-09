
# simple fizzbuzz in python
# for x in range(1, 101):
#     output = ""
#     if x % 3 == 0:
#         output += "Fizz"
#     if x % 5 == 0:
#         output += "Buzz"
#     if len(output) == 0:
#         output += str(x)
#     print(output)

#fizzbuzz as function returning a single formatted string
def fizzbuzz(intlist):
    output = ""
    for x in intlist:
        if x % 3 != 0 and x % 5 != 0:
            output += str(x)
        else:
            if x % 3 == 0:
                output += "Fizz"
            if x %5 == 0:
                output += "Buzz"
        output += "\n"
    return output

print(fizzbuzz(range(1, 21)))
