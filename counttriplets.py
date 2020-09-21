
def countTriplets(arr, r):
        count = 0
        dict = {}
        dictPairs = {}

        for i in reversed(arr):
                if i*r in dictPairs:
                        count += dictPairs[i*r]
                if i*r in dict:
                        dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

                dict[i] = dict.get(i, 0) + 1

        return count


#enter the following inputs:
#r = the common ratio
#arr = array of n numbers

r = 2
arr = [1,2,2,4]

ans = countTriplets(arr, r)

print(ans)
