"""
Functions to de-clutter the main file.
"""

constantine = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""  # this is the cow


def check_input(input: list[str]):
    if len(input) <= 1:
        print(
            """\
You didn't include anything for the cow to say!
The cow will remember this transgression..."""
        )
        exit()

