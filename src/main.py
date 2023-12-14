import math


def find_the_longest_wire(distance, list_of_pillar):
    length = 0
    if len(list_of_pillar) <= 50:
        is_element_limit = True
        for i in list_of_pillar:
            if not (1 <= i <= 100):
                is_element_limit = False
                break
        if is_element_limit:
            is_last_was_changed_to_one = False
            for index, i in enumerate(list_of_pillar):
                if index != len(list_of_pillar) - 1:
                    if is_last_was_changed_to_one:
                        if list_of_pillar[index + 1] > 1:
                            length += math.sqrt((list_of_pillar[index + 1] - 1) ** 2 + distance ** 2)
                        else:
                            length += distance
                        is_last_was_changed_to_one = False
                    else:
                        with_no_changes = math.sqrt((list_of_pillar[index + 1] - i) ** 2 + distance ** 2)
                        with_changes = math.sqrt((1 - i) ** 2 + distance ** 2)
                        if with_changes > with_no_changes:
                            is_last_was_changed_to_one = True
                            length += with_changes
                        else:
                            length += with_no_changes
    return length
