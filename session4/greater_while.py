listA=[24,12,21,16,57]
large=listA[0]
index=1
while index<len(listA):
    if listA[index]>large:
        large=listA[index]
    index+=1
print("largest sigit is:",large)
