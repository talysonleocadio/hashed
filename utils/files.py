import os

HASH_FILE_PATH = os.path.join(os.environ.get('HOME'), '.hashed_texts')


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(path, file_name):
    return os.path.join(path, file_name)


def append_content_to_file(content, file_path=HASH_FILE_PATH):
    with open(file_path, 'a+') as file:
        file.write(f'{content}\n')


def get_file_content():
    with open(HASH_FILE_PATH, 'r') as file:
        return (line for line in file.read().splitlines())


def hash_file_exists():
    return os.path.isfile(HASH_FILE_PATH)
