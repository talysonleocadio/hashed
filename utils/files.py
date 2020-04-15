import os


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(path, file_name):
    return os.path.join(path, file_name)


def file_exists(abs_file_path):
    return os.path.isfile(abs_file_path)


def append_content_to_file(file_path, content):
    with open(file_path, 'a+') as file:
        file.write(content)


def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def has_some_offensive_pointer(off_file_list):
    return any(len(file.split('.')) > 1 and file.split('.')[-1] == 'dat'
               for file in off_file_list)


def get_fortunes_from_file_list(file_list):
    files_set = {file.split('.')[0]
                 for file in file_list}
    return list(files_set)
