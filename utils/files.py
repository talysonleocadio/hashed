import os


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(file_name, path):
    return os.join(path, file_name)
