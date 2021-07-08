#---------------------------------------------------------------------------------
#Program tentang number Jump#
#Program Bilangan Ganjil#
print("1. Number jump ")
print("\ta)", end=" ")
for i in range(1, 21, 2):
    print(i, end=" ")
#---------------Akhir Program Bilangan Ganjil-------------------------------------#    


#Program bilangan genap#
print("\n\tb)", end=" ")
for i in range(2, 22, 2):
    print(i, end=" ")
#-----------------Akhir Program Bilangan Genap----------------------------------#    

print("\n\tc)", end=" ")
repeat = -1
h = 0 
for i in range(10):
    repeat += 1
    i = h + repeat
    h += repeat
    print(i, end=" ")

print("\n\td)", end=" ")
i = 0
repeat = 0
for i in range(10):
    repeat += 1
    i = repeat*repeat
    print(i, end=" ")

#Program Fibonacci#
#--------------------------------------------------------------------------------------
print("\n\n2. Fibbonaci program ")
first_number = int(input("Input the first number: "))     #Input first number
second_number = int(input("Input the second number: "))   #Input Second number
length = int(input("Input the length of fibonacci? "))    #Input length fibonacci
third_number = first_number + second_number               #formula of fibonacci

print(first_number)
print(second_number)
print(third_number)
for i in range(length - 3):                                #Process count fibonacci
             first_number = second_number
             second_number = third_number
             third_number = first_number + second_number
             print(third_number)                           #end process

#--------------------------------------------------------------------------------
#Program make Pattern Using Loop

print("\n\n3. For to do")

#Triangle pattern using number
print("\ta.", end=" ")

stop = 1
for j in range(5):
    stop += 1
    if j > 0:
        print("\n\t   ", end="")
    for i in range(1, stop, 1):
        print(i, end=" ")
#---------------------------------------------------------------------------------
        
#Triangle pattern using square number
print("\n\n\tb.", end=" ")

stop = 1
for j in range(5):
    stop += 1
    if j > 0:
        print("\n\t   ", end="")
    for i in range(1, stop, 1):
        print(i*i, end=" ")
        print(end="")
#--------------------------------------------------------------------------------
#Pattern triangle             
print("\n\n\tc.", end=" ")

for i in range(1, 6, 1):
    if i > 1:
        print("\n\t", end="   ")  #make new line
    for j in range(5, i, -1):
        print(" ", end="")        #make space 
    for k in range(1, 2*i, 1):    
        print("*", end="")        #draw triangle using star  
        print(end="")

print("\n\n\td.", end=" ")

for i in range(1, 6, 1):
    if i > 1:
        print("\n\t", end="   ")
    print(" " * (5 - i), end="")
    print("*" * ((2 * i) - 1), end="")
    
print("\n\t", end="   ")
for i in range(1, 5, 1):
    if i > 1:
        print("\n\t", end="   ")
    print(" " * i, end="")
    print("*" * (8 - (2 * i) + 1), end="")

print("\n\n\te.", end="")

for i in range(1, 6, 1):
    if i > 1:
        print("\n\t", end="  ")
    print(" " * i, end="")
    print("*" * (10 - (2 * i) + 1), end="")

print("\n\t", end="   ")
for i in range(1, 5, 1):
    if i > 1:
        print("\n\t", end="   ")
    print(" " * (4 - i), end="")
    print("*" * ((2 * i) + 1), end="")
      
        
