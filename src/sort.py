#  MIT (c) jtankersley 2019-05-18


def _swap_list_items(list, a, b):
    saved = list[a]
    list[a] = list[b]
    list[b] = saved


def sort_bubble(list = []):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                _swap_list_items(list, i, j)
    return list


def sort_instant(list = []):
    list.sort()
    return list


def sort_merge(list = []):
    list.sort()
    return list


def sort_quick(list = []):
    list.sort()
    return list
