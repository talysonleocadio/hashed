import os


def digest_exists_in_file(file_content, hexdigest):
    return hexdigest in file_content
