#this program will remove all vowels from a passed in string.
def disemvowel(string):
    return string.translate(None, "aeiouAEIOU")
