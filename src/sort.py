#  MIT (c) jtankersley 2019-05-18


def _swap_list_items(list, a, b):
    saved = list[a]
    list[a] = list[b]
    list[b] = saved


def sort_bubble(unordered_list = []):
    ordered_list = unordered_list.copy()
    for i in range(0, len(unordered_list)):
        for j in range(i, len(unordered_list)):
            if ordered_list[i] > ordered_list[j]:
                _swap_list_items(ordered_list, i, j)
    return ordered_list


def sort_instant(unordered_list = []):
    ordered_list = unordered_list.copy()
    print("instant")
    return ordered_list


def sort_merge(unordered_list = []):
    ordered_list = unordered_list.copy()
    print("merge")
    return ordered_list


def sort_quick(unordered_list = []):
    ordered_list = unordered_list.copy()
    print("quick")
    return ordered_list
