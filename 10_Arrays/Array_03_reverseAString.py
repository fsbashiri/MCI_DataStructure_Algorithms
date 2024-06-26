# create a function that reverses a string:
# 'Hi my name is Andrei'
# 'ierdnA si eman ym iH'

def reverse_string(string):
    # check input
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    elif len(string) < 2:
        return string

    # # approach 1: concatenate string with +
    # out_string = ''
    # for i in reversed(range(len(string))):
    #     out_string += string[i]
    # return out_string

    # # approach 2: use list and join
    # # create an empty list
    # reverse_string = []
    # # iterate through the string
    # for i in reversed(range(len(string))):
    #     reverse_string.append(string[i])
    # out_string = ''.join(reverse_string)
    # return out_string

    # approach 3: use slicing
    return string[::-1]

    # # approach 4: use list and reverse and join
    # string = list(string)
    # string.reverse()
    # return ''.join(string)

print(reverse_string("Hi my name is Andrei"))
