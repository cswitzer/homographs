# 1. get current directory of ran python file
# 2. find both files at the file paths based on the strings passed in
# 3. if files are the same, it's a homograph

filename_one = input("Specify the first filename: ")
filename_two = input("Specify the second filename: ")

pwd = "Users\\bob"


def canon(filename_one, filename_two):
    pwdArray = pwd.split('\\')

    f1_root = check_if_root(filename_one)
    f2_root = check_if_root(filename_two)

    fileOneArray = filename_one.split('\\')
    fileTwoArray = filename_two.split('\\')

    # Splitting \Users\bob\ will place '' at front of array, so delete that
    check_first_index(fileOneArray)
    check_first_index(fileTwoArray)

    file_one_canon = []
    file_two_canon = []

    # if filenames aren't the same, they are not homographs
    if fileOneArray[-1] != fileTwoArray[-1]:
        print("not a homograph")
        return False

    if not f1_root:
        file_one_canon = pwdArray.copy()

    if not f2_root:
        file_two_canon = pwdArray.copy()

    if fileOneArray[0] == 'C:':
        fileOneArray.pop(0)
    canonize(fileOneArray, file_one_canon)

    if fileTwoArray[0] == 'C:':
        fileTwoArray.pop(0)
    canonize(fileTwoArray, file_two_canon)

    if file_one_canon == file_two_canon:
        return True
    else:
        return False


def canonize(original_path, canonized_path):
    #print("original path", original_path)
    #print("canonzied path", canonized_path)
    for element in original_path:
        if element == ".":
            continue
        elif element == "..":
            if len(canonized_path) == 0:
                continue
            else:
                canonized_path.pop()
        else:
            canonized_path.append(element)
    #print("final path", canonized_path)

    return canonized_path


def check_if_root(filename):
    if filename[0] == '\\' or filename[0:3] == 'C:\\':
        return True
    else:
        return False


def check_first_index(fileArray):
    if fileArray[0] == '':
        fileArray.pop(0)


if canon(filename_one, filename_two):
    print("These are Homographs.")
else:
    print("These are not Homographs.")
