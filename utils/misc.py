import webbrowser

import click


TWITTER_RULES_URL = ('https://help.twitter.com/en/rules-and-policies/'
                     'twitter-rules')


def open_twitter_rules():
    webbrowser.open_new_tab(TWITTER_RULES_URL)


def print_and_exit(exit_message):
    print(exit_message)
    raise SystemExit(0)


def prompt_wrapper(prompt_msg,
                   default_value,
                   choices_args=['y', 'n']):
    return click.prompt(prompt_msg,
                        default=default_value,
                        type=click.Choice(choices_args,
                                          case_sensitive=False))
