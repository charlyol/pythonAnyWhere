def create_diamond(letter):
    if letter == "A":
        return "A"

    diamond = ""
    diamond += create_line_a(letter) + "\n"
    diamond += create_body(letter)
    diamond += create_line_a(letter)

    return diamond


def create_body(letter):
    diamond = ""
    for i in range(2, (value_of(letter) + 1)):
        diamond += create_line_of_diamond(i, letter) + "\n"

    for i in range((value_of(letter) - 1), 1, -1):
        diamond += create_line_of_diamond(i, letter) + "\n"
    return diamond


def value_of(letter):
    return ord(letter) - ord("A") + 1


def create_line_a(letter):
    return " " * (value_of(letter) - 1) + chr(ord(letter) - (value_of(letter) - 1))


def create_line_of_diamond(i, letter):
    space_left = " " * (value_of(letter) - i)
    current_letter = chr(ord(letter) - (value_of(letter) - i))
    space_between = " " * (2 * (i - 2) + 1)

    return space_left + current_letter + space_between + current_letter


if __name__ == "__main__":
    print(create_diamond("Z"))
