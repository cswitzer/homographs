# 1. get current directory of ran python file
# 2. find both files at the file paths based on the strings passed in
# 3. if files are the same, it's a homograph

filename_one = input("Specify the first filename: ")
filename_two = input("Specify the second filename: ")

pwd = "C:\\Users\\Chase Switzer\\source\\Python\\Practice\\week05\\canon.py"

def canon(filename_one, filename_two):
    pwdArray = pwd.split('\\')
    print(pwdArray)
    #test.txt
    #../../cs453/week05/test.txt
    pass

canon(filename_one, filename_two)