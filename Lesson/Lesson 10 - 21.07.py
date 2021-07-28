# 10
import os

current_dir = os.getcwd()
print(current_dir)

list_dir = os.listdir("../Homework")
print(list_dir)


base_dir = "../Homework"
def get_files_from_dir(base_dir, full_path=True):
list_dir = os.listdir(base_dir)
print(list_dir)
files = []
for file_object in list_dir:
    path_object = os.path.join(base_dir, file_object)
    if os.path.isfile(path_object):
        files.append(path_object if full_path else file_object)
    return files
homeworks_files = get_files_from_dir("Homework", full_path = False)
print(homeworks_files)

def create_dir(path):
    try:
        os.mkdir("test_dir")
    except FileExistsError:
        pass

os.makedirs("test_3_dir/test_4_dir", exist_ok=True)

####################################################################
with open("Lesson 10 - 21.07.py", "r" ) as py_file:
    data = py_file.readlines()
print(data, type(data))

data.append("# FINISH")
with open("Lesson 10_new - 21.07.py", "w" ) as py_file:
    py_file.writelines(data)

for line in data:
    if len(line) > 32:
        print(line.split("\t"))

###################################################################
def create_dir(path):
    os.makedirs(path, exist_ok=True)


def create_file(path, symbol):
    filename = f"{path}/{symbol}.txt"
    with open(filename, 'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_files_in_dir(path):
    for letter in string.ascii_lowercase:
        create_file(path, letter)


def get_tanos_click(path):
    files = os.listdir(path)
    files = list(set(files))[:len(files) // 2]
    for file in files:
        os.remove(os.path.join(path, file))


# create_dir("alphabet")
create_files_in_dir("alphabet")
get_tanos_click("alphabet")


























