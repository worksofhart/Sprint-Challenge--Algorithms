'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Look for 'th' in current string, and if found return its index in index. Else return -1 in index.
    index = word.find('th')
    # If 'th' wasn't found, we're done looking
    if index is -1:
        return 0
    # If found, add 1 to our running tally, and call `count_th()` again, passing the remainder of the string after the match
    else:
        return 1 + count_th(word[index+2:])
