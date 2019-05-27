#  MIT (c) jtankersley 2019-05-18


def search_binary(ordered_list, value):
    
    def _search(ordered_list, value, low, high):
        if (high - low) > 1:
            mid = (low + high) // 2
            if value == ordered_list[mid]:
                return mid
            elif value < ordered_list[mid]:
                return _search(ordered_list, value, low, mid - 1)
            else:
                return _search(ordered_list, value, mid + 1, high)
        else:
            return low

    return _search(ordered_list, value, 0, len(ordered_list) - 1)
