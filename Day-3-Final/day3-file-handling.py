# msg = 'my name is \n Mahad'
# print(msg)

# absolute_path = 'C:\\Users\\ast\\Desktop\\Python Workshop\\Day-3-Final\\content\\data.txt'
# relative_path = 'content/data.txt'


# read the file only
# file = open('data.txt', 'r')

# print(file.read())


# if file does not exist it will create a new file
# if file exists it will overwrite the file
# file = open('data.txt', 'w')

# file.write('Hello World and hello my world')

# print('file is written successfully')


# if file does not exist it will create a new file
# if file exists it will append to the file

file = open('data.txt', 'a')
# file.write('Hello World')
# file.write('hello my world')

file.write('\nnew line')