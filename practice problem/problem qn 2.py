def rept_rem(strr):
    st=''
    for i in strr:
        if i not in st:
            st=st+i
    return st

strr='Happy New Year'
print(rept_rem(strr))