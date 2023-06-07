# Solomon Batenhorst
import random


def bubble_sort(a_list):
    """ this function is a bubble sort algorithm """
    loop = len(a_list)

    for i in range(0, loop - 1):
        swapped = False
        for j in range(0, loop - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True

        if not swapped:
            break

    return a_list


def main():
    """ this is main and it runs the program """
    max_number = 50
    list_index = 10

    random_list = [random.randint(1, max_number) for _ in range(list_index)]
    print(f"RANDOM LIST: {random_list}")

    sorted_list = bubble_sort(random_list)
    print(f"SORTED LIST: {sorted_list}")


if __name__ == '__main__':
    main()
