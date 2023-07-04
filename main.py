def main():

    file_object = open('dummy.txt', 'r')
    type(file_object)

    file_object.close()

    new_file = open('my-new-file.txt', 'w')
    new_file.write('Hello, this is my new file!')
    new_file.close()
main()