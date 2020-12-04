a = input("word")
b = ""
c = []
for i in range(len(a)):
    c.append(a[i]*2)
    b = b+ c[i]
print(b)
