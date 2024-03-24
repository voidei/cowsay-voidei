import sys
import textwrap

from thecow import check_input, constantine, increase_character

check_input(sys.argv)

params = sys.argv[1]
"""What the cow says."""


# cut at 39, but also 59?
# so like 40 is the cutoff, but 60 is the cutoff for like..single words?
def cowsay(input: str):
    """The actual cowsay function"""
    length = len(input.strip())
    say = ""
    wrapped_text = textwrap.wrap(input, width=39, break_long_words=False)

    if len(wrapped_text) == 1:
        underscore = increase_character("_", 0, length)
        dash = increase_character("-", 0, length)
        say = f""" {underscore}\n< {input} >\n {dash}{constantine}"""

    if len(wrapped_text) == 2:
        max_length = len(wrapped_text[0])
        underscore = increase_character("_", 0, max_length)
        dash = increase_character("-", 0, max_length)
        say = f"""\
 {underscore}
/ {wrapped_text[0]} \\
\\ {wrapped_text[1]:<39} /
 {dash}{constantine}"""

    if len(wrapped_text) >= 3:
        max_length = len(wrapped_text[0])
        underscore = increase_character("_", 0, max_length)
        dash = increase_character("-", 0, max_length)
        say = f"""\
 {underscore}
/ {wrapped_text[0]} \\
| {wrapped_text[1]:<39} |
\\ {wrapped_text[2]:<39} /
 {dash}{constantine}"""

    print(say)


def main():
    cowsay(params)


if __name__ == "__main__":
    main()
