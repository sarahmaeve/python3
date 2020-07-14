# https://www.youtube.com/watch?v=Bn_SJPt0ukw

def count_flips(binary_array):
    flips = 0
    register = 0b0
    for i in binary_array:
        if i != register:
            flips += 1
            register = i
    return flips

my_input = [0b0,0b0,0b1,0b1,0b1]

print(count_flips(my_input))