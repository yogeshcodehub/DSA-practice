def reverse_string(s):

    words=s.split()
    reverse_word=words[::-1]
    reversed_string=' '.join(reverse_word)
    return reversed_string

s="hii yogeshwaran how are you ?"
print(reverse_string(s))
