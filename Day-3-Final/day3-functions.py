
# def salam():
#     print('Assalamoalaikum!')

# def greet(name):
#     print('Hello World')
#     print('Hello', name)

# salam()
# greet('Anas')

# def add(x, y):
#     result = x + y
#     return result

# z = add(1, 2)
# print(z)

# big_number = z + 5
# print(big_number)

# n = None
# print(n)



# def addCandy(current_candies, number_of_big_candy=1, number_of_small_candy=4):
#     return current_candies + number_of_big_candy + number_of_small_candy


# abhi_ki_candies = 2
# # candies_needed = 5

# my_candybox = addCandy(abhi_ki_candies)

# print(my_candybox)



# my_mystory_box = [
#     'laptop',
#     'books',
#     'car',
#     'gold',
#     False,
#     1.5
# ]

# def mystorBoxOpener(items):
#     for item in items:
#         print(item)


# mystorBoxOpener(my_mystory_box)


def dynamicAdd(*numbers):
    # print(numbers)
    # print(type(numbers))
    result = 0
    for n in numbers:
        # print(result, n)
        result = result + n
    # print('summed value of result', result)
    return result

print( dynamicAdd(4, 3 ,8) )