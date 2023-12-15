import math


def find_the_longest_wire(distance, list_of_pillar):
    longest_to_top = 0
    longest_to_bottom = 0
    current_pole = 0

    while current_pole < len(list_of_pillar) - 1:
        top_to_bottom = longest_to_top + math.sqrt(distance ** 2 + (list_of_pillar[current_pole] - 1) ** 2)
        bottom_to_bottom = longest_to_bottom + distance

        bottom_to_top = longest_to_bottom + math.sqrt(distance ** 2 + (list_of_pillar[current_pole + 1] - 1) ** 2)
        top_to_top = longest_to_top + math.sqrt(
            distance ** 2 + abs(list_of_pillar[current_pole] - list_of_pillar[current_pole + 1]) ** 2)

        longest_to_top = max(bottom_to_top, top_to_top)
        longest_to_bottom = max(bottom_to_bottom, top_to_bottom)

        current_pole += 1

    return max(longest_to_top, longest_to_bottom)
