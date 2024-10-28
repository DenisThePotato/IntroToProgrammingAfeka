a = int(input("First number = "))
b = int(input("Second number = "))
c = int(input("Third number = "))
if a < b:
    if c < a:
        print(c, a, b, sep='\n')
    elif c > b:
        print(a, b, c, sep='\n')
    else:
        print(a, c, b, sep='\n')
else:
    if c < b:
        print(c, b, a, sep='\n')
    elif c > a:
        print(b, a, c, sep='\n')
    else:
        print(b, c, a, sep='\n')
