def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max1=data[0]
    for i in data:
        if max1<i:
            max1=i
    return max1
print(find_max([1,3,7,9,11]))
    