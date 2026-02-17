def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3: Only letters and numbers allowed
    if not s.isalnum():
        return False

    # Rule 4 & 5: Numbers must be at end and first number cannot be 0
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                if char == "0":
                    return False
        else:
            if number_started:
                return False

    return True


main()
