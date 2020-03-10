import os


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(file_name, path):
    return os.join(path, file_name)


def file_exists(file_path):
    return False


def append_content_to_file(file_path, content):
    return False

