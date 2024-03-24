"""
Functions to de-clutter the main file.
"""

constantine = """\
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""
"""This is the cow, his name is constantine."""


def check_input(input: list[str]):
    """Check to ensure user has given the cow something to say, exit if they haven't."""
    if len(input) <= 1:
        print(
            """\
    You didn't include anything for the cow to say!
    The cow will remember this transgression..."""
        )
        exit()


def increase_character(input: str, lower: int, upper: int):
    output = input
    for _ in range(lower, upper):
        output = output + input
    return output


def print_single_line(input: str, length: int):
    output = f"""\
  {increase_character("_", 0, length-1)}
< {input} >
  {increase_character("-", 0, length-1)}
{constantine}"""
    return output


def print_double_line(input: list[str], length: int):
    output = f"""\
  {increase_character("_", 0, length-1)}
/ {input[0]} \\
\\ {input[1].ljust(length)} /
  {increase_character("-", 0, length-1)}
{constantine}"""
    return output


def generate_first_line(input):
    dash = "-"
    underscore = "_"
    output = f"{input}"
    return output


def generate_mid_line(input: str, line_length: int, triple: bool = False):
    output = ""
    if triple:
        output = f"| {input.ljust(line_length)} |"
    if not triple:
        output = f"{input}"
    return output


def generate_last_line(input: str, line_length: int, triple: bool = False):
    output = ""
    if triple:
        output = f"\\ {input.ljust(line_length)} /"
    if not triple:
        output = f"{input}"
    return output
