"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Martin Buchal
email: buchalM@seznam.cz
discord: #buchy6031
"""
from task_template import TEXTS

login = input ("Please enter your login:\n")

password = input ("Please enter your password:\n")

registred_users = {"bob": "123",
"ann": "pass123", "mike": "password123",
"liz": "pass123"}

if login.lower () in registred_users:
    stored_password = registred_users [login.lower()]
    if password == stored_password:
        print (40*"-")
        print (f"Welcome to the app, {login.capitalize()}!")
        print (40*"-")
        text_number = input ("There are 3 text to analyze.\nPlease choose one of them by entering nb.: 1, 2 or 3\n")
        print (40*"-")
        if text_number.isdigit ():
            text_number = int(text_number)
            if text_number >= 1 and text_number <= 3:
                print ("Please see the text analysis below:\n")
                text_to_analyze = TEXTS [int (text_number) - 1]

                words = text_to_analyze.split ()

                word_count = len(words)
                words_capitalized = 0
                words_upper = 0
                words_lower = 0
                number_count = 0
                number_sum = 0

                for word in words:
                    word = word.strip (",.")
                    if word.istitle ():
                        words_capitalized += 1
                    if word.isupper ():
                        words_upper += 1
                    if word.lower ():
                        words_lower += 1
                    if word.isnumeric ():
                        number_count += 1
                        number_sum += int (word)

                print (f"There are {word_count} words in the text that you've chosen.")
                print (f"Also you can find {words_capitalized} titlecase words there.")
                print (f"Number of uppercase words is: {words_upper}")
                print (f"Number of lowercase words is: {words_lower}")
                print (f"Number of number in text is: {number_count}")
                print (f"Sum of number in text is: {number_sum}")

                word_length_counts = {}
                for word in words:
                    length = len(word)
                    word_length_counts[length] = word_length_counts.get(length, 0) + 1

                print (40*"-")
                print ("LEN|"," OCURENCES","   |NR.")
                print (40*"-")
                for length, count in sorted(word_length_counts.items()):
                    print(f"{length:2}|{'*' * count:15}|{count:3}")
            else:
                print (f"\nI'm sorry {login.capitalize()}, but your input wasn't a number between 1 and 3.\nPlease try again.\nProgram shutting down..\n")
        else:
            print (f"\nI'm sorry {login.capitalize()}, but your input wasn't in expected format.\nPlease try again.\nProgram shutting down..\n")

    else:
        print (f"Non-registred user or wrong password.\nProgram shutting down..")
else:
    print (f"Non-registred user or wrong login.\nProgram shutting down..")