def unique_list(nums):
    #here is creating a list with unique elements
    result = []
    for num in nums:
        if num not in result:
            result.append(num)

    return result
print(unique_list([1, 2, 2, 3, 3, 4]))
print(unique_list([1, 1, 2, 3, 2]))