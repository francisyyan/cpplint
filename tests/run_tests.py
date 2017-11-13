#!/usr/bin/env python

import sys
import os
from os import path
import re
from helpers import output


def assert_errors(output, errors_expected):
    m = re.search(r'Total errors found: (0|[1-9][0-9]*)', output)
    errors_found = int(m.group(1))

    if errors_found != errors_expected:
        sys.exit('Expect %d errors but found %d\n' %
                 (errors_expected, errors_found))


def main():
    cpplint = path.join(
        path.join(path.dirname(path.abspath(__file__)), os.pardir),
        'cpplint.py')

    assert_errors(output([cpplint, 'good_braces.cc']), 0)
    assert_errors(output([cpplint, 'bad_braces.cc']), 6)


if __name__ == '__main__':
    main()
