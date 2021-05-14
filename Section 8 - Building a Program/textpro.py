five_Ws = ("Who", "What", "When", "Where", "Why", "How")
final_sentence = ""

def sen_maker(string):
    if string.capitalize().startswith(five_Ws):
        string = "%s? " %string.capitalize()
    else:
        string = "%s. " %string.capitalize()
    
    return string


user_input = input("Say something or enter '\end' to quit: ")

while user_input != "\end":
    final_sentence += sen_maker(user_input)

    user_input = input("Say something or enter '\end' to quit: ") 


print(final_sentence)
