def has_negatives(a):
    #input and output will be an array of numbers
    num_dict = {}

    for num in a:
        if num not in num_dict:
            num_dict[num] = None
        if (num * -1) in num_dict:
            num_dict[num*-1] = num
            num_dict[num] = num *-1

    result = []
    for num in num_dict:
        if num > 0 and num_dict[num] is not None:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
