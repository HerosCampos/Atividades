import os

path_to_file = os.path.join(os.path.dirname(__file__), 'data.txt')


my_file = open(path_to_file, 'r')
file_content = my_file.read()
my_file.close()

print(file_content)


name = input('Enter user name: ')
file_writing = open(path_to_file, 'w')
file_writing.write(name)
file_writing.close()



































