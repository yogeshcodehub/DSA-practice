def largest_odd(s):

    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
s="123456"
print(largest_odd(s))