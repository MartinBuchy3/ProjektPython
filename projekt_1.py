"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Martin Buchal
email: buchalM@seznam.cz
discord: #buchy6031
"""
def main ():
    from task_template import TEXTS
    number_of_texts = len (TEXTS)
    login = input ("Please enter your login:\n").lower ()
    password = input ("Please enter your password:\n").lower ()
    registred_users = {"bob": "123",
    "ann": "pass123", "mike": "password123",
    "liz": "pass123"}

    if login in registred_users and password == registred_users [login]:
        print (40*"-")
        print (f"Welcome to the app, {login.capitalize()}!")
        print (40*"-")
        text_number = int(input(f"There are {number_of_texts} texts to analyze.\nPlease choose one of them by entering a number (1-{number_of_texts}): "))
        print (40*"-")
        def text_analysis ():
            while True:
                try:
                    if 1 <= text_number <= number_of_texts:
                        print ("Please see the text analysis below:")
                        print (40*"-")
                        text_to_analyze = TEXTS [int (text_number) - 1]
                        words = text_to_analyze.split ()
                        word_count = len(words)
                        words_capitalized = sum (1 for word in words if word.istitle())
                        words_upper = sum (1 for word in words if word.isupper())
                        words_lower = sum (1 for word in words if word.islower())
                        numbers = [int(word) for word in words if word.isnumeric()]
                        number_count = len(numbers)
                        number_sum = sum(numbers)
                        print (f"There are {word_count} words in the text that you've chosen.")
                        print (f"Also you can find {words_capitalized} titlecase words there.")
                        print (f"Number of uppercase words is: {words_upper}")
                        print (f"Number of lowercase words is: {words_lower}")
                        print (f"Amount of numbers in text is: {number_count}")
                        print (f"Sum of number in text is: {number_sum}")
                    
                        word_length_counts = {}
                        for word in words:
                            length = len(word)
                            word_length_counts[length] = word_length_counts.get(length, 0) + 1    
                        print (40*"-" + "\n", "LEN|"," OCURENCES"," |NR.\n", 40*"-") 

                        for length, count in sorted(word_length_counts.items()):
                            print(f"{length:2}|{'*' * count:15}|{count:3}")  
                        break        
                    else:
                        print (f"\nI'm sorry {login.capitalize()}, but your input wasn't a number between 1 and {number_of_texts}.\nPlease try again.\nProgram shutting down..\n")
                        break
                except ValueError:
                    print (f"\nI'm sorry {login.capitalize()}, but your input wasn't in expected format.\nPlease try again.\nProgram shutting down..\n")
                    break
        text_analysis ()
    else:
        print (f"Non-registred user, please try again.\nProgram shutting down..")
if __name__ == "__main__":
    main()