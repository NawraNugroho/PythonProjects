print(
    """
                      Welcome to GCF and LCM program

        In this program you can find the GCF (greatest common factor)
        and LCM (least common multiple) of TWO number. Input
        "0" in the "first number" prop to exit. """)


first_number = None

while first_number != 0:
    first_number = int(input("\n\nInput the first number: "))
    if first_number == 0:
        break
    else:
        second_number = int(input("Input the second number: "))

    if second_number > first_number:
        biggest_number = second_number
    else:
        biggest_number = first_number

    for i in range(1, biggest_number + 1):
        if first_number%i == 0 and second_number%i == 0:
            GCF = i

    for j in range(biggest_number, first_number*second_number+1):
        if j%first_number == 0 and j%second_number == 0:
            LCM = j
            break

    print("\nGCF of", first_number, "and", second_number, "is", GCF)
    print("LCM of", first_number, "and", second_number, "is", LCM)



