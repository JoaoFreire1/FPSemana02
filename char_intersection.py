a = input()
a1 = a.split (" ")
set1 = set(a1)
b = input()
b1 = b.split (" ")
set2 = set(b1)

same = (set1).intersection(set2)
print(" ".join(same))