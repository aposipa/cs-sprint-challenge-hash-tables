def get_indices_of_item_weights(weights, length, limit):
    #weights is an array of numbers
    #length and limit are numbers
    weight_dict = {}

    for i in range(len(weights)):
        if weights[i] not in weight_dict:
            weight_dict[weights[i]] = [i]
        else:
            weight_dict[weights[i]].append(i)

    result = [-1,-1]
    for weight in weight_dict:
        if (limit-weight) in weight_dict:
            if weight == limit-weight:
                result[0] = weight_dict[weight][0]
                result[1] = weight_dict[limit-weight][1]
            else:
                result[0] = weight_dict[weight][0]
                result[1] = weight_dict[limit-weight][0]

    if -1 not in result:
        result.sort(reverse=True)
        return result

    #output is an array of numbers unless it's empty then it's None
    return None


'''
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
'''

## Hints
 
# A brute-force solution would involve two nested loops, yielding a
#   quadratic-runtime solution. How can we use a hash table in order to
#   implement a solution with a better runtime?

# Think about what we can store in the hash table in order to help us to
#   solve this problem more efficiently. 

# What if we store each weight in the input list as keys? What would be
#   a useful thing to store as the value for each key? 

# If we store each weight's list index as its value, we can then check
#   to see if the hash table contains an entry for `limit - weight`. If it
#   does, then we've found the two items whose weights sum up to the
#   `limit`!
