key = [3,1]
usb = [5,2,8]
budget = 10
cost = 0

maxkey = max(key)

maxusb = max(usb)
print(maxkey)
print(maxusb)

usb.sort()
print(usb)

if ((min(key)+min(usb)) > budget):
    cost = -1
elif maxkey > maxusb:
    print("key is more")
    cost = maxkey + min(usb)
elif maxusb > maxkey:
    print("usb is more")
    cost = maxusb + min(key)

print(cost)


#this solution doesn't work if the maximum cost of one item is greater than
#the budget
#def getMoneySpent(keyboards,drives,b):

""" Hackerrank solution

"""

