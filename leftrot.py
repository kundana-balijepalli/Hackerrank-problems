a = [1,2,3,4,5]
d = 4


tempa = [0]*len(a)
print(tempa)
i = 0

while i < (len(a)):
    new_ind = (i + d)%len(a)
    tempa[i] = a[new_ind]
    i+= 1

print(tempa)
