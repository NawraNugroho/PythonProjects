#triangle
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
print("----------TRIANGLE----------")
length = int(input("length(number only): "))

for i in range(1, length+1, 1):
    print(" " * length, end="") #space
    print("* " * i) #stars
    length -= 1
    

#diamond
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
print("\n\n----------DIAMOND----------")
length = int(input("Length(number only): "))
length2 = length

for i in range(1, length+1, 1):
    print(" " * length, end="") #space
    print("* " * i) #stars
    length -=1

for i in range(1, length2, 1):
    print(" " * (i+1), end="")
    print("* " * (length2-1))
    length2 -= 1


#
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
print("\n\n----------HOURGLASS----------")
length = int(input("Length(number only): "))
length2 = length

for i in range(1, length+1, 1):
    print(" " * i, end="") #space
    print("* " * length) #stars
    length -= 1

for i in range(1, length2, 1):
    print(" " * (length2-1), end="")
    print("* " * (i+1))
    length2 -= 1
    
