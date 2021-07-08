BMI_average = []

choice = ""

while choice != "exit":
    average = 0
    
    print("Enter 'add' to add a variable. \nEnter 'average' to show an average. \nOr enter 'exit' to exit.")

    choice = input("\nYour choice: ")

    if choice.lower() == "add":
        height = float(input("\nEnter your height in meter: "))
        weight = float(input("Enter your weight in kilogram: "))
        BMI = weight/(height*height)
        BMI_average.append(BMI)
        
        if BMI < 16:
            print("You are severly underweight.\n\n")
        elif BMI < 18.5 and BMI >= 16:
            print("You are underweight.\n\n")    
        elif BMI < 25 and BMI >= 18.5:
            print("You are normal.\n\n")    
        elif BMI < 30 and BMI >= 25:
            print("You are overweight.\n\n")    
        elif BMI >= 30:
            print("You are obese.\n\n")

    elif choice.lower() == "average":
        for item in BMI_average:
            average += item
        average /= len(BMI_average)

        if average < 16:
            print("The average of people are severly underweight (", average, ")")    
        elif average < 18.5 and average >= 16:
            print("The average of people are underweight (", average, ")")        
        elif average < 25 and average >= 18.5:
            print("The average of people are normal (", average, ")")     
        elif average < 30 and average >= 25:
            print("The average of people are overweight (", average, ")")
        elif average >= 30:
            print("The average of people are obese (" + average + ")")
            
        
        
            
