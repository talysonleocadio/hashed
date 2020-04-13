import subprocess

from shutil import which


def main():
    if which("fortune") is None:
        raise Exception("""Fortune is not installed on your sistem,
                        please install it before continuing""")

    fortune_args = ["fortune", "50%", "funny", "50%", "not-funny"]
    stdout = subprocess.run(fortune_args, capture_output=True)


if __name__ == '__main__':
    main()
