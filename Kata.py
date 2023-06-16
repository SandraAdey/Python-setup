#Reversing words in a string
#Hello everyone = everyone hello

import string


def reverse(st):
    lst = string.split(" ")
    lst.reverse()
    reversed_string = " ".join(lst)
    print(reversed_string)

