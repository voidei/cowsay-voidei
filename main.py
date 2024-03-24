import sys
import textwrap

constantine = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""  # this is the cow
# print(len(sys.argv))
# print(sys.argv)

if len(sys.argv) <= 1:
    print(
        "You didn't include anything for the cow to say!\nThe cow will remember this transgression..."
    )
    exit()
params = sys.argv[1]


# cut at 39, but also 59?
# so like 40 is the cutoff, but 60 is the cutoff for like..single words?
def cowsay(input: str):
    """The actual cowsay function"""
    length = len(input.strip())
    underscore = "_"
    dash = "-"
    say = ""
    max_width = 39
    wrapped_text = textwrap.wrap(input, max_width)
    if len(wrapped_text) == 1:
        for _ in range(0, length):
            underscore = underscore + "_"
            dash = dash + "-"
        say = f""" {underscore}\n< {input} >\n {dash}{constantine}"""

    if len(wrapped_text) == 2:
        max_length = len(wrapped_text[0])
        for _ in range(0, max_length):
            underscore = underscore + "_"
            dash = dash + "-"
        say = f"""\
 {underscore}
/ {wrapped_text[0]} \\
\\ {wrapped_text[1]:<39} /
 {dash}{constantine}"""

    if len(wrapped_text) >= 3:
        print(">3 todo")

    print(say)


def main():
    cowsay(params)


if __name__ == "__main__":
    main()
