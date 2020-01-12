#  MIT (c) jtankersley 2019-05-18


def binary_search(orderedList, value):
    
    def _search(orderedList, value, low, high):
        if (high - low) > 1:
            mid = (low + high) // 2
            if value == orderedList[mid]:
                return mid
            elif value < orderedList[mid]:
                return _search(orderedList, value, low, mid - 1)
            else:
                return _search(orderedList, value, mid + 1, high)
        else:
            return low

    return _search(orderedList, value, 0, len(orderedList) - 1)
