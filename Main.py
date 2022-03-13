from random import randint
import sys

def Main():
    answer = ''
    while answer != "goodbye":
        answer = str(input()).lower()
        if answer == "goodbye":
            print("Okay, bye then! ")
            sys.exit()

        if inQuestions(answer, questions):
            print(base_questions(answer, questions))
        else:
            print(reflect(answer, reflections))
        


def inQuestions(answer, questions):
    for elem in questions.keys():
        if elem in answer:
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
            if words[i] in keys:
                words[i] = dict[words[i]]
        return ' '.join(words)


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

if __name__ == '__main__':
    print("Hello, i'm Eliza, how are you doing today? ")
    Main()