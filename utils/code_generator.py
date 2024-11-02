import itertools
import string


def generate_codes(start="AAAAAAA"):
    # Create the character set for codes (letters and numbers)
    charset = string.ascii_uppercase + string.digits  # 'A-Z' and '0-9'

    # Find the length of the code
    length = len(start)

    # Create an iterator to generate combinations
    combinations = itertools.product(charset, repeat=length)

    # Start from the given initial code
    started = False
    for combo in combinations:
        code = "".join(combo)
        if code == start:
            started = True
        if started:
            yield code
