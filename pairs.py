ar = [10,20,20,10,10,30,50,10,20]
n = 9

pairs = 0

for i in ar[:]:
    pairs += ar.count(i)//2
    while i in ar:
        ar.remove(i)
print(pairs)

            
