from question_two_list_of_cities import cities_list


def count_number_repetitions():
    city_num_operations = {}
    for city in cities_list:
        try:
            city_num_operations[city[0]] += 1
        except KeyError:
            city_num_operations[city[0]] = 1
    return city_num_operations


# this lets us use the number of operations as the key to find the Nth most operation
def inverse_dict(city_num_operations):
    num_operations_for_city = {}
    for k, v in city_num_operations.items():
        num_operations_for_city[v] = num_operations_for_city.get(v, []) + [k]
    return num_operations_for_city


def get_max_operations(num_operations_for_city):
    num_operations = num_operations_for_city.keys()
    max_operations = max(num_operations)
    return num_operations_for_city[max_operations]


def get_closest(number, list_operations):
    return min(list_operations, key=lambda x: abs(x - number))


def part_one():
    def _city_values(cities):
        for city in cities:
            print(f"City name: {city}")

    print("Part One:")
    city_to_operations_dict = count_number_repetitions()
    operations_to_city_dict = inverse_dict(city_to_operations_dict)

    requested_number_of_operations = int(input("Input Number Of Police Operations: "))
    if requested_number_of_operations in operations_to_city_dict.keys():
        _city_values(operations_to_city_dict[requested_number_of_operations])
    elif requested_number_of_operations == 0:
        max_operation = get_max_operations(operations_to_city_dict)
        _city_values(max_operation)
    else:
        print("Number of operations not in list provided, giving nearest approximate: ")
        closest_num_ops = get_closest(requested_number_of_operations, operations_to_city_dict.keys())

        print(
            f"Cities: {operations_to_city_dict[closest_num_ops]},"
            f"Operations: {closest_num_ops}"
        )


def part_two():
    print("""
Part Two
    I think think the best way to find the safest city would be to:
    1) given the city with the lowest number of police operations
    2) if multiple values are given from (1), then find the city with the oldest year applicable
    3) if there is a tie in (2), then list all applicable cities
    4) given location information (outside of scope), give distance to each city
    """)

if __name__ == '__main__':
    part_one()
    part_two()