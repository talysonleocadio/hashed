from shutil import which
import webbrowser

import click

from utils import files, hashes, fortunes



def main():
    if which("fortune") is None:
        raise Exception("Fortune is not installed on your sistem,"
                        " please install it before continuing")

    greetings()


@click.command()
@click.option('--confirm',
              'confirmation',
              prompt=('\nGreetings! do you like to post some fortune'
                      ' on your twitter account today?'),
              type=click.Choice(default_option_choices, case_sensitive=False),
              default='y',
              help='Confirm that you wanna post on Twitter')
def greetings(confirmation):
    if confirmation == 'n':
        print('\nIf you like to post some stuff, comeback again later!')
        raise SystemExit(0)

    fortune_msg = get_random_fortune()
    print(f'Here we go! The fortune msg is:\n{fortune_msg}')

    default_value, choices = 'y', ['y', 'n', 'see']
    post_confirmation = prompt_wrapper(
        ('Some content may hurt people feelings.'
         ' Before you post I recomend you to read the policies'
         ' Type <see> to read Twitter policies'),
        default_value, choices)

    while post_confirmation == 'see':
        open_twitter_rules()
        default_value = 'y'
        post_confirmation = prompt_wrapper('All right! Do you wanna post?',
                                           default_value)

        # Try to post tweet with the fortune
        # In case of success, write the digest to hash files


def get_random_fortune():
    print('Getting a nice random fortune...\n')
    fortune_msg = fortunes.get_random_fortune()
    print('Checking if this fortune has been posted previously...\n')
    fortune_already_posted = check_if_hash_exists_in_file(fortune_msg)

    if files.hash_file_exists() and fortune_already_posted:
        retry_confirmation = prompt_wrapper(
            ('Oops! The fortune has already posted.'
             ' Do you wanna try again?\n'),
            'y', default_option_choices)

        if retry_confirmation == 'n':
            print('\n All right then, comeback again later!')
            raise SystemExit(0)

        get_random_fortune()

    return fortune_msg


def check_if_hash_exists_in_file(fortune_msg):
    fortune_digest = hashes.sha1_hex_digest(fortune_msg)

    try:
        return fortune_digest in files.get_file_content()
    except (FileNotFoundError, OSError):
        return False


if __name__ == '__main__':
    greetings()
