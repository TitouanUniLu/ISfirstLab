from random import randint

def Main():
    answer = ''
    while answer != "goodbye":
        answer = str(input())
        if answer in possible_answer:
            rand = randint(0,1)
            print(possible_answer[answer][rand])
            print(possible_answer.keys())

#i feel happy

subject = ["I", "me", "us", "we"]
sad_emotions = ["sad", "depressed", "angry"]
happy_emotions = ["good", "fine", "alright"]
default_answers = ["Tell me more...", "Are you sure about that? ", "What makes you feel that way"]

possible_answer = {
    'i feel': ['why do you feel', "it's strange that you feel"]
}


if __name__ == '__main__':
    print("Hello, i'm Eliza, how are you doing today? ")
    Main()


"""
answer = str(input())
        if answer == "goodbye":
            print('see ya buddy! ')
        elif answer in happy_emotions:
            print('It is good that you are', answer, "! ")
        elif answer in sad_emotions:
            print(' :( thats rough buddy')
        else:
            rand = randint(0,2)
            print(default_answers[rand])
"""