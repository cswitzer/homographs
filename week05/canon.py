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
    filename_match_check(fileOneArray, fileTwoArray)

    file_one_canon = copy_pwd_if_root(f1_root, pwdArray)
    file_two_canon = copy_pwd_if_root(f2_root, pwdArray)

    pop_letter_drive(fileOneArray)
    pop_letter_drive(fileTwoArray)

    canonize(fileOneArray, file_one_canon)
    canonize(fileTwoArray, file_two_canon)

    if file_one_canon == file_two_canon:
        return True
    else:
        return False


def check_if_root(filename):
    if filename[0] == '\\' or filename[1:3] == ':\\':
        return True
    else:
        return False


def check_first_index(fileArray):
    if fileArray[0] == '':
        fileArray.pop(0)


def copy_pwd_if_root(file_root, pwdArray):
    if not file_root:
        return pwdArray.copy()
    else:
        return []


def filename_match_check(fileOneArray, fileTwoArray):
    if fileOneArray[-1] != fileTwoArray[-1]:
        return False


def pop_letter_drive(file_array):
    if file_array[0][1] == ":":
        file_array[0] = file_array[0][2:]
        check_first_index(file_array)


def canonize(original_path, canonized_path):
    # print("original path", original_path)
    # print("canonzied path", canonized_path)
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
    # print("final path", canonized_path)

    return canonized_path


if canon(filename_one, filename_two):
    print("These are Homographs.")
else:
    print("These are not Homographs.")
