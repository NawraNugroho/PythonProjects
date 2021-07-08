# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:49:04 2021

@author: pc
"""

#PROBABILITY CALCULATOR
#Create a lottery ball, or Hat, 
#that takes a variable number of arguments 
#that specify the number of balls of each color that are in the hat. 
#Give the object the ability to pick a random number of balls from the hat, 
#which will then be used to compute the probability 
#of picking a certain distribution of balls over a large number of experiment

#CALCULATION PROBABILITY: of color: self.color/self.total
#                         of number: amount of balls that include those number/self.total
#                         of that color and number: 1/self.total

#initial value description:
#   realmax(color) are the original maximum value and the original total amount of a color (ball)
#   amount(color) are the amount/total of specific color balls (decreasing over time)
#   total is the original total amount of all balls

import random

class Lottery_ball(object):
    def __init__(self, max_redball, max_yellowball, max_blueball, amount_red, amount_yellow, amount_blue):
        """The blue print of lottery ball generator"""
        self.realmaxred = max_redball
        self.realmaxyellow = max_yellowball
        self.realmaxblue = max_blueball
        self.amountred = amount_red
        self.amountyellow = amount_yellow
        self.amountblue = amount_blue

        self.total = amount_red + amount_yellow + amount_blue
        
    def pick_ball(self, exception_list):
        """Generate a random ball"""
        exception = exception_list #dictionary with list as its value
        number = 0
        color = ["red", "yellow", "blue"]
        color_pick = random.choice(color)
        
        while number == 0:
            #Try to pick a different number if the same color with the same number has been generated already
            if color_pick == "red":
                #keep searching for number that's not in exception dictionary list
                while number in exception["red"]:
                    if len(exception["red"])-1 == self.realmaxred:
                        while color_pick == "red":
                            color_pick = random.choice(color)
                        break
                    else:
                        number = random.randint(1, self.realmaxred)
                    
            elif color_pick == "yellow":
                #keep searching for number that's not in exception dictionary list
                while number in exception["yellow"]:
                    if len(exception["yellow"])-1 == self.realmaxyellow:
                        while color_pick == "yellow":
                            color_pick = random.choice(color)
                        break
                    else:
                        number = random.randint(1, self.realmaxyellow)
            
            elif color_pick == "blue":
                #keep searching for number that's not in dictionary exception list
                while number in exception["blue"]:
                    if len(exception["blue"])-1 == self.realmaxblue:
                        while color_pick == "blue":
                            color_pick = random.choice(color)
                        break
                    else:
                        number = random.randint(1, self.realmaxblue)
                
                
        exception[color_pick].append(number)
        
        print("You got a ball with a color", color_pick, "and number", number)
        return color_pick, number, exception
        
        
    def __str__(self,color_pick,number_pick, exception_list):
        """Display the informatian of a certain ball"""
        prob_col,prob_num,prob_ball = self.__probability(color_pick, number_pick, exception_list)
        return "The probability of picking a color "+color_pick+" is "+str(prob_col)+"\nThe probability of picking a number "+str(number_pick)+" is "+str(prob_num)+"\nThe probability of picking a color "+color_pick+" and a number "+str(number_pick)+" is "+str(prob_ball)

        
    def __probability(self, color, number, exception_list):
        """Count the probability"""
        exception = exception_list
        
        #Probability of picking a color
        if color == "red":
            prob_col = round(self.amountred/self.total*100, 2)
        elif color == "yellow":
            prob_col = round(self.amountyellow/self.total*100, 2)
        elif color == "blue":
            prob_col = round(self.amountblue/self.total*100, 2)

            
        #probability of picking a number
        amount = 0
        if self.realmaxred >= number:
            if (number not in exception["red"]) or (color == "red"):
                amount += 1
        if self.realmaxyellow >= number:
            if (number not in exception["yellow"]) or (color == "yellow"):
                amount += 1
        if self.realmaxblue >= number:
            if (number not in exception["blue"]) or (color == "blue"):
                amount += 1
        
        prob_num = round(amount/self.total*100, 2)
        
        #probability of picking specific ball
        prob_ball = round(1/self.total*100, 2)
        
        return prob_col, prob_num, prob_ball
    

def main():
    realmax_red = int(input("The total amount of red ball: "))
    realmax_yellow = int(input("The total amount of yellow ball: "))
    realmax_blue = int(input("The total amount of blue: "))
    
    exception = {"red" : [0],
                 "yellow" : [0],
                 "blue" : [0]}

    
    amount_red = realmax_red
    amount_yellow = realmax_yellow
    amount_blue = realmax_blue
    
    res = int(input("Press 1 to generate, press 0 to exit: "))
    
    while res != 0:
        ball1 = Lottery_ball(realmax_red, realmax_yellow, realmax_blue, amount_red, amount_yellow, amount_blue)
        color_pick, number_pick, exception = ball1.pick_ball(exception)
        print(ball1.__str__(color_pick, number_pick, exception))
        
        if color_pick == "red":
            amount_red -= 1
        elif color_pick == "yellow":
            amount_yellow -= 1
        elif color_pick == "blue":
            amount_blue -= 1
        
        res = int(input("Press 1 to generate, press 0 to exit: "))

        
main()
        
