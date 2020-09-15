import click
from utils import files, hashes, misc


@click.command()
@click.option('--confirm',
              'confirmation',
              prompt=('\nGreetings! do you like to transform some text'
                      ' in a hash digest?'),
              type=click.Choice(['y', 'n'], case_sensitive=False),
              default='y',
              help='Confirm that you wanna transform some text in digest')
def greetings(confirmation):
    if confirmation == 'n':
        misc.print_and_exit('\nAlright then, see ya!')

    get_user_input()


def get_user_input():
    user_input = click.prompt('Text that you wanna to hash')
    hash_exists_in_file = check_if_hash_exists_in_file(user_input)

    if (hash_exists_in_file):
        misc.print_and_exit('\nThis text digest already exists in file.'
                            ' Please, try another one.')

    input_digest = hashes.sha1_hex_digest(user_input)
    files.append_content_to_file(input_digest)

    print(f'The digest: {input_digest} was successfully written to file: '
          f'{files.HASH_FILE_PATH}')


def check_if_hash_exists_in_file(user_input):
    fortune_digest = hashes.sha1_hex_digest(user_input)

    try:
        return fortune_digest in files.get_file_content()
    except (FileNotFoundError, OSError):
        return False


if __name__ == '__main__':
    greetings()
