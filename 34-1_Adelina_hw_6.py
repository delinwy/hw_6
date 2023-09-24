def bubble_sort(list1):
    n = len(list1)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return f'Отсортированный список: {list1}'


def binary_search(list1, element):
    first = 0
    last = len(list1) - 1
    result_ok = False
    pos = -1
    while first <= last:
        middle = (first + last) // 2
        if element == list1[middle]:
            result_ok = True
            pos = middle
            break
        elif element > list1[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f'Элемент {element} найден в позиции: {pos}.')
    else:
        print(f'Элемент {element} не найден.')


unsorted_list = [23, 35, 2, 12, 45, 13, 7]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

element_to_find = 35
binary_search(unsorted_list, element_to_find)

