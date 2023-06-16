#Reversing words in a string
#Hello everyone = everyone hello
def reverse(str):
    return " ".join(reversed(str.split())).split()
