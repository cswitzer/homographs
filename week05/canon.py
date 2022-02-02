# 1. get current directory of ran python file
# 2. find both files at the file paths based on the strings passed in
# 3. if files are the same, it's a homograph

from fileinput import filename


filename_one = input("Specify the first filename: ")
filename_two = input("Specify the second filename: ")

pwd = "C:\\Users\\Chase Switzer\\source\\Python\\Practice\\"

def canon(filename_one, filename_two):
    pwdArray = pwd.split('\\')
    #test.txt
    #..\..\Python\Practice\test.txt

    fileOneArray = filename_one.split('\\')
    fileTwoArray = filename_two.split('\\')
    
    
    

    pass

canon(filename_one, filename_two)