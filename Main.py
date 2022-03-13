from random import randint
import sys

def Main():
    answer = ''
    '''while answer != "goodbye":
        answer = str(input())
        answered = False
        if answer == "goodbye":
            print("Okay, bye then! ")
            sys.exit()
        for elem in all_default:
            if elem in answer:
                first = answer[:(len(elem))]
                rest = answer[len(elem):]
                rand = randint(0,len(possible_answer[first])-1)
                print(possible_answer[first][rand], rest)
                answered = True
                break
        if not answered:
            print(default_answers[randint(0,len(default_answers)-1)])'''

    def reflect(answer, dict):
        words = answer.lower().split()
        keys = dict.keys();
        for i in range(0, len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
        return ' '.join(words)


    x = str(input())
    print(reflect(x, reflections))

subject = ["I", "me", "us", "we"]
sad_emotions = ["sad", "depressed", "angry","bad"]
happy_emotions = ["good", "fine", "alright"]
default_answers = ["Tell me more...", "Are you sure about that? ", "What makes you feel that way"]

possible_answer = {
    'i feel': ['why do you feel', "it's strange that you feel"],
    'i think': ['why do you think', "it's strange that you think"],
    'i have': ['since when do you have', 'do you really have']
}

def get_List(dict):
    return dict.keys()
all_default = get_List(possible_answer)

reflections = {
  "am": "are",
  "was": "were",
  "i": "you",
  "we" : "you",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "i will": "you will",
  "my": "your",
  "are": "am",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me",
  "me": "you"
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