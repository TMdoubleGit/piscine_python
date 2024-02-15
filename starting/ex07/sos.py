import sys

NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/'
}


def main():
    ac = len(sys.argv)
    try:
        assert ac == 2, "AssertionError: the arguments are bad"
        j = sum(not (c.isalpha() or c.isspace() or c.isdigit())
                for c in sys.argv[1])
        if j > 0:
            raise AssertionError("AssertionError: the arguments are bad")
        to_convert = sys.argv[1].upper()
        converted = ' '.join(NESTED_MORSE[c] for c in to_convert)
        print(converted)

    except AssertionError as e:
        print(e)


if (__name__ == "__main__"):
    main()
