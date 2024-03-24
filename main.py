import sys

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
    if length < 39:
        for _ in range(0, length):
            underscore = underscore + "_"
            dash = dash + "-"

    say = f""" {underscore}\n< {input} >\n {dash}{constantine}"""

    print(say)


def main():
    cowsay(params)


if __name__ == "__main__":
    main()
