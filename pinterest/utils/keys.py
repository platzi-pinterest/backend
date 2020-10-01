#! /usr/local/bin/python3

"""Secrets generator."""

import argparse
import base64
import hashlib
import secrets


def setup_args_parser():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        choices=[256, 512, 1024, 2048, 4096],
        help='Random bits to be used for key generation.',
        type=int,
        default=4096
    )

    parser.add_argument(
        '-a',
        type=str,
        choices=[
            'bits',
            'int',
            'md5',
            'md5base64',
            'sha256',
            'sha256base64',
            'sha512',
            'sha512base64'
        ],
        help='Select algorith to encode output.',
        default='sha512base64'
    )

    parser.add_argument(
        '-s',
        type=str,
        help='Optional text to hash using one encoding option.'
    )

    args = parser.parse_args()
    return args


def gen_key(length, alg, text=None):
    """Generate key using user's input."""
    m = text if text else bin(secrets.randbits(length))[2:]

    if alg == 'bits' and not text:
        return m

    if alg == 'int' and not text:
        return int(m, 2)

    if alg == 'md5':
        h = hashlib.md5(str.encode(m))
        return h.hexdigest()

    if alg == 'md5base64':
        h = hashlib.md5(str.encode(m))
        return base64.b64encode(h.digest()).decode()

    if alg == 'sha256':
        h = hashlib.sha256(str.encode(m))
        return h.hexdigest()

    if alg == 'sha256base64':
        h = hashlib.sha256(str.encode(m))
        return base64.b64encode(h.digest()).decode()

    if alg == 'sha512':
        h = hashlib.sha512(str.encode(m))
        return h.hexdigest()

    if alg == 'sha512base64':
        h = hashlib.sha512(str.encode(m))
        return base64.b64encode(h.digest()).decode()


if __name__ == '__main__':
    """Main method."""

    args = setup_args_parser()
    if args.s:
        key = gen_key(args.l, args.a, text=args.s)
    else:
        key = gen_key(args.l, args.a)
    print(key)
