import random
import subprocess

import utils.files as files

FORTUNES_FILE_PATH = '/usr/share/fortune'


def get_fortune_message():
    fortune = _get_random_fortune()
    fortune_args = _gen_fortune_args(fortune)


def _get_random_fortune():
    file_list = files.get_file_list(FORTUNES_FILE_PATH)
    fortunes = files.get_fortunes_from_file_list(file_list)
    return random.choice(fortunes)


def _gen_fortune_args(fortune_arg):
    return f'fortune {fortune_arg} -s'.split(' ')
