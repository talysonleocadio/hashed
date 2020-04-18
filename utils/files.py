import os

HASH_FILE_PATH = os.path.join(os.environ.get('HOME'), '.hashed_fortunes')


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(path, file_name):
    return os.path.join(path, file_name)


def append_content_to_file(file_path, content):
    with open(file_path, 'a+') as file:
        file.write(content)


def get_file_content():
    with open(HASH_FILE_PATH, 'r') as file:
        return (line for line in file.read().splitlines())


def get_fortunes_from_file_list(file_list):
    files_set = {file.split('.')[0]
                 for file in file_list}
    return list(files_set)


def hash_file_exists():
    return os.path.isfile(HASH_FILE_PATH)
