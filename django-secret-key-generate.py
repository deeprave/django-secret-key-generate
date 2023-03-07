#!/usr/bin/env python
"""
Generate a secret key for Django
"""
import random
import string

# keep this plain, avoid chars requiring escapes
LETTERS = string.ascii_letters + string.digits


def secret_key(length: int = 50):
    return ''.join(random.choice(LETTERS) for _ in range(length))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-l', '--length', type=int, action='store', default=50,
                        help='Length of the secret key')
    parser.add_argument('-e', '--env', action='store_true', default=False,
                        help='Generate as environment variable')

    args = parser.parse_args()

    key = secret_key(args.length)
    if args.env:
        key = f'SECRET_KEY="{key}"'
    print(key)
