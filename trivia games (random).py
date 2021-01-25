import random

much = 0
correct = 0
Exit = 0
player_answer = ""

question = ["How many string are in a violin (number only)? ", "What is the capital city of England? ", "How many sides are in a pentagon (number only)? ",
            "Who are Harry Potter's two best friends? (letter only) \nA)Ron and Hermione B)Fred and George C)Ginny and Cho ",
            "Who sang Shut Up and Dance? ", "What are the genre of the song Firework? (letter only) \nA)Folk B)Blues ",
            "In the movie Ferdinand, who is Ferdinand best friend? ", "Who played Stephen Hawking in The Theory of Everything (first and last name only)? ",
            "What does hashtag (#) mean in music? ", "When is American independence day (month and date only)? ", "How many cents are in a dime (number only)? ",
            "What is the theme song of Zootopia? ", "Who played the role of Captain Jack Sparrow in the Pirates of The Caribbean movie (first and last name only)? ",
            "When is April Fools Day (month and date only)? ", "When was the Frozen movie released (number only)? ", "How many days are in a week (number only)? ",
            "Who invented the light bulb (first and last name only)? ", "What does hashtag (#) mean in python? ", "In what month is winter in USA (one month only)? ",
            "What color does red and yellow makes when it's mix together? ",
            "What are the three primary colors? (letter only) \nA)Black, white and blue B)Red, blue and yellow ", "What is the biggest planet? ",
            "Which programming languange that's widely used to make Google? ", "What is the landmark of America in New York Harbor? ",
            "What is the next prime number after 89 (number only)? ", "In computer keyboard, which key is used to make an uppercase letter? ", 
            "What does AKA stand for? ", "What is the antonym of 'fake'? ", "What does PC stand for? ",
            "A word that has a same sound, but has a different meaning and spelling is called what? ", "What's the biggest city in Australia? ",
            "Who's Sofia's sister name in Sofia The First? ", "When was YouTube invented? (letter only) \nA)2000 B)2003 C)2005 D)1998 ",
            "When was Google invented? (letter only) \nA)2000 B)2003 C)2005 D)1998 ", "What's the capital of Massachusetts? ",
            "Which Ed Sheeran album contain Thinking Out Loud song? (letter only) \nA)Divide B)X C)+ ",
            "Who is the first president of America (first and last name only)? ", "Who is the composer of Twinkle Twinkle Little Star (last name only)? ",
            "In what year did the French gave the statue of liberty to US? (letter only) \nA)1776 B)1876 C)1886 ", "When was the song Roar released (number only)? ",
            "How many hours are there in a week (number only)? ", "What stands for International System of Units? ",
            "Clarinet is what type of aerophone instrument? (letter only) \nA)Brass B)Woodwind C)Free-reed ", "Which state is the first state in America? ",
            "When is UK independence day (month and date only)? ", "Which are we gonna focus on first when we hear a song? (letter only) \nA)Melody B)Harmony ",
            "What song was the winner of Grammy Award for Song of the Year 2008? ", "Where do macaroni penguin live? ",
            "What is the smallest country in the world? (letter only) \nA)Lebanon B)Nauru C)Vatican City ", "Is the word 'prodigy' a noun a verb or an adjective? "]
    
answer = ["4", "London", "5", "A", "Walk The Moon", "A", "Nina", "Eddie Redmayne", "Sharp", "July 4", "10", "Try Everything", "Johnny Depp", "April 1",
          "2013", "7", "Thomas Edison", "Comment", "December", "Orange", "B", "Jupiter", "Python", "Statue of Liberty", "97", "Caps Lock", "As known as",
          "Real", "Personal Computer", "Homophone", "Sydney", "Amber", "C", "D", "Boston", "B", "George Washington", "Mozart", "C", "2013", "168", "SI", "B",
          "Delaware", "May 1", "A", "Viva La Vida", "Antarctic Peninsula", "C", "Noun"]

#pick any random question without repeating
while len(question) != 0:
    number = random.randrange(0, len(question))

               #50-30 = 20 (questions)
    if much < (len(question) - 30):
        much += 1
    else:
        break
    
    answer_choice = answer[number]
    question_choice = question[number]
    player_answer = input(question_choice)
    
    if player_answer.lower() == answer_choice.lower():
        print("Correct\n")
        correct += 1
    elif player_answer.lower() == "exit":
        Exit += 1
        break
    else:
        print("Wrong! The answer is", answer_choice, "\n")

    del question[number]
    del answer[number]

#tell the user their score
if Exit == 1:
    Score = 100 * correct // (much - 1)
    print("\nYou got", Score, "% right :)")
elif Exit == 0:
    Score = 100 * correct // much  
    print("\nYou got", Score, "% right :)")
        

                          
    




