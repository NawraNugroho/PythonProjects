pascal = []


length = int(input("Length: "))
for i in range(0, length):
    element = []
    for j in range(0, i+1):
        if j==0 or j==i:
            element.append(1)
        else:
            value = pascal[i-1][j-1] + pascal[i-1][j]
            element.append(value)
            
    pascal.append(element)


space = length*3

for k in range(length):
    print("\n", " " * space, end="")
    for l in range(k+1):
        print(pascal[k][l], end="     ")
    space -= 3  
