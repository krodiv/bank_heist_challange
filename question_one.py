from multiprocessing import Pool


def check_if_6_digits(str_number):
    if len(str_number) == 6:
        return True
    else:
        return False


def check_correct_range(number):
    if 146810 < number < 612564:
        return True
    else:
        return False


# since the operations are very similar in resources used,
# I've combined criteria three and four together into one function
def check_same_adjacent_numbers(str_number):
    has_duplicate_digits = False
    increasing_digits = True
    for i in range(len(str_number) - 1):
        # Third criteria
        if str_number[i] == str_number[i + 1]:
            has_duplicate_digits = True
        # Fourth criteria
        if not int(str_number[i]) <= int(str_number[i + 1]):
            increasing_digits = False
    return has_duplicate_digits and increasing_digits


def passing_criteria(number):
    str_number = str(number)
    first_check = check_if_6_digits(str_number)
    second_check = check_correct_range(number)
    third_and_fourth_check = check_same_adjacent_numbers(str_number)
    return first_check and second_check and third_and_fourth_check


def part_one():
    count = 0
    for i in range(146810, 612564):
        if passing_criteria(i):
            count += 1
    print(f"Total number of combinations for part one: {count}")


def part_two():
    with Pool() as p:
        value = p.map(passing_criteria, range(146810, 612564))
        count = sum(value)
        print(f"Total number of combinations for part two: {count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
    part_two()
