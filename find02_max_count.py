def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    min1=data[0]
    for i in data:
        if min1>i:
            min1=i
    return min1
print(find_max_count([1,3,7,9,11]))
