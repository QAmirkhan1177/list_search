def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    min1=data[0]
    for i in data:
        if min1>i:
            min1=i
    return min1
print(find_min([1,3,7,9,11]))
    