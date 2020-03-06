from unittest import TestLoader, TextTestRunner


def run_tests():
    testsuite = TestLoader().discover('./tests',
                                      top_level_dir='./',
                                      pattern='*.py')
    TextTestRunner(verbosity=4).run(testsuite)


if __name__ == '__main__':
    run_tests()
