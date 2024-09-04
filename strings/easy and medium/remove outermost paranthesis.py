def remove_paranthesis(s):

    if s.startswith('(') and s.endswith(')'):
        return s[1:-1]
    return s
s='(hii yogesh)'
print(remove_paranthesis(s))