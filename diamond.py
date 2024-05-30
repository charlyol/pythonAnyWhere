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


def create_body_full(letter):
    diamond = ""
    for i in range(2, (value_of(letter) + 1)):
        diamond += create_line_of_diamond_full(i, letter) + "\n"

    for i in range((value_of(letter) - 1), 1, -1):
        diamond += create_line_of_diamond_full(i, letter) + "\n"
    return diamond


def create_line_of_diamond_full(i, letter):
    space_left = " " * (value_of(letter) - i)
    current_letter = chr(ord(letter) - (value_of(letter) - i))
    space_full = ""
    for i in range(ord(letter) - 1, 0, -1):
        space_full += chr(i)
    for i in range(ord(letter)):
        space_full += chr(i)
    return space_left + current_letter + space_full + current_letter


def create_diamond_full(letter):
    index = ord(letter)
    diamond = ""
    diamond += create_line_a(letter) + "\n"
    diamond += create_body_full(letter)
    diamond += create_line_a(letter)
    return diamond


print(ord("a"))


# if __name__ == "__main__":
#     print(create_diamond("A"))
#     print(create_diamond("B"))
#     print(create_diamond("C"))
#     print(create_diamond("D"))
#     print(create_diamond("E"))
#     print(create_diamond("F"))
#     print(create_diamond("G"))
#     print(create_diamond("H"))
#     print(create_diamond("I"))
#     print(create_diamond("J"))
#     print(create_diamond("K"))
#     print(create_diamond("L"))
#     print(create_diamond("M"))
#     print(create_diamond("N"))
#     print(create_diamond("O"))
#     print(create_diamond("P"))
#     print(create_diamond("Q"))
#     print(create_diamond("R"))
#     print(create_diamond("S"))
#     print(create_diamond("T"))
#     print(create_diamond("U"))
#     print(create_diamond("V"))
#     print(create_diamond("W"))
#     print(create_diamond("X"))
#     print(create_diamond("Y"))
#     print(create_diamond("Z"))
