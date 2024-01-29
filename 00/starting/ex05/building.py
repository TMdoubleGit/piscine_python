import sys


def main():
    """
    This program takes a string as parameters and displays the count
    of characters, upper and lower letters, punctuation marks,
    spaces and digits.

    It reads the string character by character and uses basic methods
    such as isdigit(), isupper(), islower() or isspace()
    to increment counters.
    """
    ac = len(sys.argv)
    try:
        if (ac == 2):
            text = sys.argv[1]
        elif (ac == 1):
            print("What is the text to count?")
            text = ""
            while True:
                try:
                    char = sys.stdin.read(1)
                    if not char or char == '\x04':
                        break
                    text += char
                except EOFError:
                    break
        else:
            raise AssertionError("More than one argument is provided")

        assert text, "Please provide a non-empty string"

        index = digit = upper = lower = space = punct = 0
        while (index < len(text)):
            if (text[index].isdigit() == 1):
                digit += 1
            elif (text[index].isupper() == 1):
                upper += 1
            elif (text[index].islower() == 1):
                lower += 1
            elif (text[index].isspace() == 1):
                space += 1
            else:
                punct += 1
            index += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")

    except AssertionError as e:
        print(e)


if (__name__ == "__main__"):
    main()
