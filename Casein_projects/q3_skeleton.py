def f1(s):
    return len(s)

def f2(s):
    return s[int(len(s)/2)]

def f3(s):
    return s[0: int(len(s)/2): 2]

def f4(s):
    return s[int(len(s)/2):]

def f5(s1,s2):
    return (s1 + s2)

def f6(s):
    res = -1
    res = (len(s) % 2 == 0)
    return res

def f7(s):
    return s[len(s)-1:0:-1]

def f8(s):
    return s[:int(len(s)/2)-1] == s[len(s)-1:int(len(s)/2):-1]