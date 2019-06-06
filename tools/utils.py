import os
import tools.constant as constant


def list_to_str(list):
    separator = ','
    str_list = []
    for member in iter(list):
        str_list.append(str(member))
    member_tuple = tuple(str_list)
    return separator.join(member_tuple)


def read_file(file_path):
    file = []
    with open(file_path) as f:
        for line in f:
            file.append(line.rstrip())
    return file


def write_file(file_name, obj):
    path = os.path.join(constant.data_files_path, file_name)
    with open(path, 'w')as f:
        for line in obj:
            f.write(line + '\n')
    print("Save" + file_name + 'in to' + path)
