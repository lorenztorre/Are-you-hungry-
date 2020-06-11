word = input('Are you hungry?\n\n')
yes = "\nThere's food at home."
no = "\nThen shut up."
new_word = [] # this will save the 'for loop' into here, porting each result from the loop into this list

def hungry_question(word): 
    for letter in word: # 'letter' here is just the name we are giving to our variable ## result from 'word' (remember this is an input method) will be fed into this loop
        if letter.isalpha() == True: # method .isalpha() is checking all index points of answer from 'word' to look for alphacharacters ## so it's saying if the letter is an actual letter
            new_word.append(letter) # we are saving the results from our 'letter' loop test to a new variable called 'new_word'
    
    word = "".join(new_word) # variable 'word' will be all of the joined characters gathered from the for loop, compiled to the 'new_word' variable, and joined together to create the new word, or in this case, answer 

     
    if word.lower() == 'yes':
        print(yes)
    elif word.lower() == 'no':
        print(no)
    else:
        print('Make up your damn mind.')

hungry_question(word)