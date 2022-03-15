from random import randint
import sys

def Main():
    answer = ''
    while answer != "goodbye":
        answer = str(input()).lower()
        if answer == "goodbye":
            print("Okay, bye then! ")
            sys.exit()

        elif inGreetings(answer, greetings):
            for elem in greetings.keys():
                if elem in answer:
                    print(greetings.get(elem))

        elif inQuestions(answer, questions):
            print(base_questions(answer, questions))

        elif inReflections(answer, reflections):
            print(reflect(answer, reflections))

        else:
            print(default_answers[randint(0,len(default_answers)-1)])
            
            
        

def inGreetings(answer, greetings):
    for elem in greetings.keys():
        if elem in answer:
            return True

def inQuestions(answer, questions):
    for elem in questions.keys():
        if elem in answer:
            return True

def inReflections(answer, reflections):
    words = answer.lower().split()
    keys = reflections.keys()
    for i in range(0, len(words)):
        for elem in keys:                
            if words[i] == elem:
                return True

def base_questions(answer, questions):
    for elem in questions.keys():
        if elem in answer:
            rest = answer.replace(elem, "")
            return (questions.get(elem) + rest).replace("  ", " ")


def reflect(answer, dict):
        words = answer.lower().split()
        keys = dict.keys()
        for i in range(0, len(words)):
            for elem in keys:
                if words[i] == elem:
                    words[i] = dict[words[i]]
        return ' '.join(words)

greetings = {
    "hello": "hello how are you? ",
    "my name is": "hi, my name is eliza, how are you? ",
    "hi": "hello there, what is your name?"
}

questions = {
    "i want": "why do you want ",
    "i feel": "why makes you feel",
    "i think": "what makes you think",
    "i believe in": "interesting belief, why do you believe",
    "i need": "would it really help you to get",
    "i can't": "what do you think is the reason you can't"
}

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

default_answers = ["i have no idea what you're talking about...", "maybe try saying something simpler?", 
                    "sorry i don't understand, try saying something else", "i'm not smart enough to answer that sorry"]

if __name__ == '__main__':
    print("Hello, i'm Eliza, how are you doing today? ")
    Main()