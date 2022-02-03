# 1. get current directory of ran python file
# 2. find both files at the file paths based on the strings passed in
# 3. if files are the same, it's a homograph

from fileinput import filename


filename_one = input("Specify the first filename: ")
filename_two = input("Specify the second filename: ")

pwd = "C:\\Users\\Chase Switzer\\source\\Python\\Practice\\week05"

def canon(filename_one, filename_two):
    pwdArray = pwd.split('\\')

    #test.txt
    #..\..\Python\Practice\test.txt

    fileOneArray = filename_one.split('\\')
    fileTwoArray = filename_two.split('\\')

    print(fileTwoArray)

    biggest_array_size = 0

    if len(fileOneArray) >= len(fileTwoArray):
        biggest_array_size = len(fileOneArray)
    else:
        biggest_array_size = len(fileTwoArray)

    # if filenames aren't the same, they are not homographs
    if fileOneArray[-1] != fileTwoArray[-1]:
            return False

    # check for ./
    for i in range(len(fileOneArray)):
        print(i)
    # check for ../

canon(filename_one, filename_two)