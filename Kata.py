#Reversing words in a string

import string


def reverse(st):
    lst = string.split(" ")
    lst.reverse()
    reversed_string = " ".join(lst)
    print(reversed_string)

