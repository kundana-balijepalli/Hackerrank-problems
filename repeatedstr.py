s = 'aba'
n = 10

str = s*(n//len(s))
lastseg = s[:n%len(s)]
print(str)
print(lastseg)
