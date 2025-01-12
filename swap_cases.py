# Function to swap the letters
def swap_case(s):
    # list to add the converted
    new_list = []
    # make the string into a list to iterate
    letters = list(s)
    # abc = 'abcdefghijklmnopqrstuvwxyz' # use in previous solution

    for char in letters:
        # if char in abc:
        if char.islower():
            new_list.append(char.upper())
        # elif char in abc.upper():
        elif char.isupper():
            new_list.append(char.lower())
        else:
            new_list.append(char)

    return ''.join(new_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
