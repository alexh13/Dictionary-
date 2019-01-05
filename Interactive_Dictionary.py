import json
from difflib import get_close_matches

data = json.load(open("data.json"))  # open json dictionary containing word:definition pairs


def translate(w):
    w = w.lower()  # Converts parameter to lower case
    if w in data:  # if the word is in data -
        return data[w]  # return that word's data
    elif w.title() in data: # if user enters a proper noun this will check for a capitol first letter
        return data[w.title()] # when data with capitol letter is found return that data's definition
    elif w.upper() in data: # if input data is a word with all upper case the program will check for that in the data
        return data[w.upper()] # returns that upper case word's definition
    elif len(get_close_matches(w, data.keys())) > 0:
        userMeant = input("Did you mean %s instead? Enter Y if yes, or N if no: "
                          % get_close_matches(w, data.keys())[0])
        if userMeant == "Y":
            return data[get_close_matches(w, data.keys())[0]] # returns closest matched word's data if user inputs Y
        elif userMeant == "N":
            return "This word doesn't exist. Please double check it." # if user inputs N returns string
        else:
            return "We didn't understand your entry."
    else:  # user input a word that doesn't match in dictionary
        return "This word doesn't exist. Please double check it."


word = input("Enter a word to look up: ")
runFunction = translate(word)  #  Assigned function to variable runFunction for use in a conditional statement

if type(runFunction) == list: # if the type returned from the function is a list then run the for loop
    for item in runFunction: # for loop runs through function data output(a list) and prints each definition line by
        # line
        print(item)
else: # the type returned from the function is NOT a list print the output
    print(runFunction)

