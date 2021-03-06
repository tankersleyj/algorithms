#  MIT (c) jtankersley 2019-05-18


def bubble_sort(list):
    # Only viable for very short lists

    def _swap_list_items(list, a, b):
        saved = list[a]
        list[a] = list[b]
        list[b] = saved

    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                _swap_list_items(list, i, j)
    return list


def merge_sort(list):
    # O(n log n) sort of list via divide and merge

    def _merge(list, low, mid, high):
        new_list = []
        orig_low = low
        orig_mid = mid
        for i in range(orig_low, high + 1):
            if low < orig_mid and (mid > high or list[low] <= list[mid]):
                new_list.append(list[low])
                low += 1
            elif mid <= high and (low >= orig_mid or list[mid] <= list[low]):
                new_list.append(list[mid])
                mid += 1
        for i in range(0, len(new_list)):
            list[orig_low + i] = new_list[i]

    def _sort(list, low, high):
        mid = (low + high) // 2
        if (mid - low) > 0:    
            _sort(list, low, mid)
        if (high - (mid + 1)) > 0:    
            _sort(list, mid + 1, high) 
        _merge(list, low, mid + 1, high)

    if len(list) > 1:
        low = 0
        high = len(list) - 1
        mid = (low + high) // 2
        _sort(list, low, mid)
        _sort(list, mid + 1, high)
        _merge(list, low, mid + 1, high)
    return list


def python_sort(list):
    list.sort()
    return list
