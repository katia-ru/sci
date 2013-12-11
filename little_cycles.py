in_file = open("out_qmbn", "r")
my = {}
for ii in in_file:
    k = ii.split()
    l = len(k)
    if my.has_key(l):
        my[l] += 1
    else:
        my[l] = 1

for jj in my:
    print jj, my[jj]
