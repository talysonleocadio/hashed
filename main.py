import os
import subprocess
from shutil import which
import webbrowser

import click
from colorama import init as init_colorama, Fore, Style

from utils import files, hashes, fortunes

init_colorama(autoreset=True)

FORTUNES_FILE_PATH = '/usr/share/fortune'
OFF_FILE_PATH = os.path.join(FORTUNES_FILE_PATH, 'off')
default_option_choices = ['y', 'n']
app_settings = {}


def main():
    if which("fortune") is None:
        raise Exception("Fortune is not installed on your sistem,"
                        " please install it before continuing")

    greetings()

    # fortune_args = ["fortune", "50%", "funny", "50%", "not-funny"]
    # stdout = subprocess.run(fortune_args, capture_output=True)


@click.command()
@click.option('--confirm',
              'confirmation',
              prompt=('\nGreetings! do you like to post some fortune'
                      ' on your twitter account today?'),
              type=click.Choice(default_option_choices, case_sensitive=False),
              default='y',
              help='Confirm that you wanna post on Twitter')
@click.option('--off-fortunes',
              'offensive',
              prompt='Do you like to use Potentially offensive fortunes?',
              type=click.Choice(default_option_choices, case_sensitive=False),
              default='n',
              help='Confirm that you wanna use offensive fortunes')
def greetings(confirmation, offensive):
    if confirmation == 'n':
        print('\nIf you like to post some stuff, comeback again later!')
        raise SystemExit(0)

    off_files = os.listdir(OFF_FILE_PATH)
    are_offs_available_to_use = files.has_some_offensive_pointer(off_files)
    if are_offs_available_to_use and offensive == 'y':
        print(f'\n{Fore.YELLOW}{Style.BRIGHT}WARNING: '
              f'{Style.RESET_ALL}Potentially Offensive fortunes are available.'
              ' Do you really like to use them?')

        default_value, choices = 'n', ['y', 'n', 'see']
        off_confirmation = click_prompt_wrapper(
            ('Offensive content may hurt people feelings.'
             ' Type <see> to read Twitter policies'),
            default_value, choices)

        while off_confirmation == 'see':
            open_twitter_rules()
            default_value = 'n'
            off_confirmation = click_prompt_wrapper('Are you sure about to post offensive fortunes?',
                                                    default_value)


def click_prompt_wrapper(prompt_msg, default_value, choices_args=default_option_choices):
    return click.prompt(prompt_msg,
                        default=default_value,
                        type=click.Choice(choices_args,
                                          case_sensitive=False))


def open_twitter_rules():
    twitter_rules_url = ('https://help.twitter.com/en/rules-and-policies/'
                         'twitter-rules')
    webbrowser.open_new_tab(twitter_rules_url)


if __name__ == '__main__':
    greetings()
