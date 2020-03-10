import os


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content


def get_absolute_file_path(path, file_name):
    return os.path.join(path, file_name)


def file_exists(abs_file_path):
    return os.path.isfile(abs_file_path)


def append_content_to_file(file_path, content):
    try:
        with open(file_path, 'a+') as file:
            file.write(content)
    except FileNotFoundError as error:
        print(f"File does not exist: {error}")
