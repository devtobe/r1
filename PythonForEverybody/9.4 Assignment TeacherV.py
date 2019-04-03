fname = input("Enter a file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

dic = dict()

for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        dic[w] = dic.get(w, 0) +1

print(dic)

big_value = 0
for key, value in dic.items():
    if big_value < value:
        big_value = value
        big_key = key

print(big_key, big_value)


