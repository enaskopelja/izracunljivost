import argparse


def _my_divmod(x, y):
    q, r = divmod(x, y)
    return (q, r) if r else (q - 1, y)


def _divide(number, basis):
    if number:
        while number:
            number, remainder = _my_divmod(number, basis)
            yield remainder
    else:
        yield 0


def main(*, alphabet: str, **kwargs):
    alphabet = "ε" + alphabet
    try:
        code = int(input("Type the number you wish to decode: ").strip())
        if code < 0:
            raise ValueError("Code should be unsigned")
    except ValueError as e:
        raise ValueError("Please input an unsigned integer") from e

    return "".join(reversed([alphabet[i] for i in _divide(code, len(alphabet) - 1)]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--alphabet',
        required=True
    )

    print(main(**vars(parser.parse_args())))
