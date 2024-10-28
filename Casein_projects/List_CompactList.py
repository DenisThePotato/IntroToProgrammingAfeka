def compact_list(list):
    for i in range (len(list)):
        if list[i] == '0':
            for j in range(i+1, len(list)):
                if list[j] != '0':
                    list[i] = list[j]
                    list[j] = '0'
                    break

list = ['0', '0', '8', '8', '0', 'b']
print(list)
compact_list(list)
print(list)