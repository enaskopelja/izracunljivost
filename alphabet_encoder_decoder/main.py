import argparse
import decode
import encode

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--action',
        choices=['encode', 'decode'],
        required=True
    )

    parser.add_argument(
        '--alphabet',
        required=True
    )

    arguments = parser.parse_args()
    if arguments.action == 'encode':
        print(encode.main(**vars(arguments)))
    else:
        print(decode.main(**vars(arguments)))
