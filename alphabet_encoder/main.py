import argparse


def main(*, alphabet: str):
    word = input("Type the word you wish to encode: ").strip()
    alphabet = sorted(alphabet)
    try:
        codings = [alphabet.index(c) + 1 for c in word]
    except ValueError as e:
        raise ValueError("Word contains letters outside alphabet") from e
    return sum(len(alphabet) ** i * c for i, c in enumerate(reversed(codings)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--alphabet',
        help='Alphabet',
        dest="alphabet",
        required=True
    )

    print(main(**vars(parser.parse_args())))
