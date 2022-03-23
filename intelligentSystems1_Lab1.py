from random import randint
import sys

def Main():
    answer = ''
    print("         -- Welcome to the Eliza bot --")
    print("Please try and use simple sentences because Eliza is not the smartest")
    print("If you want to leave, just tell eliza goodbye :)")
    print("----------------------------------------------")
    print("Hello, i'm Eliza, I am a therapy bot. How are you doing? ")

    while answer != "goodbye":
        answer = str(input()).lower()
        if answer == "goodbye":
            print("Okay, bye then! ")
            sys.exit()

        elif inGorQ(toString(answer), greetings):
            for elem in greetings.keys():
                if elem in answer:
                    print(greetings.get(elem))
                    break

        elif inGorQ(answer, questions):
            print(base_questions(answer, questions))

        elif checkEmotions(answer, emotions):
            continue

        elif inReflections(answer, reflections):
            if not inGorQ(answer, commonAnswers):
               print(reflect(answer, reflections, True))
            else:
                comAnsw(answer, commonAnswers)

        elif inGorQ(answer, commonAnswers):
            comAnsw(answer, commonAnswers)

        else:
            print(default_answers[randint(0,len(default_answers)-1)])
             

def inGorQ(answer, dictionary):
    for elem in dictionary.keys():
        if elem in answer:
            return True

def comAnsw(answer, dict):
    for elem in commonAnswers.keys():
        if elem in answer:
            print(commonAnswers.get(elem))
            break

def toString(answer):
    words = answer.lower().split()
    return words

def inReflections(answer, reflections):
    words = toString(answer)
    keys = reflections.keys()
    for i in range(0, len(words)):
        for elem in keys:                
            if words[i] == elem:
                return True

def base_questions(answer, questions):
    for elem in questions.keys():
        if elem in answer:
            rest = answer.replace(elem, " ")
            rest = reflect(rest, reflections, False) #added this so when the user says "i think i am sad", instead of asnwering why do you think i am sad?" it says "why do you think you are sad"
            return (questions.get(elem) + " " + rest + "?").replace("  ", " ")


def reflect(answer, dict, reflectWithQuestion):
        words = answer.lower().split()
        keys = dict.keys()
        for i in range(0, len(words)):
            for elem in keys:
                if words[i] == elem:
                    words[i] = dict[words[i]]
                    break
            if words[i] == elem: #added another if statement to avoid going through the whole dictionary when a match is found
                    break
        if reflectWithQuestion:
           return ' '.join(words) + '. Do yo think that is a good thing or not?'
        else:
            return ' '.join(words)

def checkEmotions(answer, emotions):
    for elem in emotions:
        if elem in answer and 'not' not in answer:
             print("Why are you feeling", elem)
        elif elem in answer and 'not' in answer:             
            print(default_answers[randint(0,len(default_answers)-1)])
        else:
            continue
        return True

greetings = {
    "hello": "hello how are you? ",
    "my name is": "hi, my name is eliza, how are you? ",
    "hi": "hello there, how are you feeling?",
    "hey": "hello there, how do you do?"
}

emotions = ['great', 'awesome', 'good', 'bad', 'fine', 'amazed', 'happy', 'aggravated', 'anxious', 'attractive', 'awful', 'awestruck', 'bold', 'chilly', 'bashful', 'brave', 'dejected', 
'cautious', 'bubbly', 'dirty', 'composed', 'cheerful', 'dreadful', 'easygoing', 'comfortable', 'heavy', 'horrified', 'delightful', 
'irritated', 'intelligent', 'excited', 'pessimistic', 'numb', 'festive', 'tearful', 'puzzled', 'free', 'tense', 'quizzical',
'jolly', 'terrible', 'ravenous', 'optimistic', 'tired', 'reluctant', 'proud', 'ugly', 'settled', 'wonderful', 'weak', 'shy',
'agreeable', 'annoyed', 'ambivalent', 'animated', 'bitter', 'anxious', 'bright', 'disgruntled', 'bashful', 'clever', 'disgusted', 
'candid', 'encouraging', 'evil', 'cautious', 'fresh', 'guilty', 'horrified', 'gentle', 'hostile', 'intelligent', 'hopeful', 'hurtful',
 'mysterious', 'kind', 'nasty', 'pragmatic', 'loving', 'obnoxious', 'political', 'open', 'oppressive', 'quizzical', 'pleased', 
 'overbearing', 'religious', 'supportive', 'resentful', 'secretive', 'sympathetic', 'sarcastic', 'secular', 'warm', 'sardonic',
  'strong', 'amazed', 'aggravated', 'anxious', 'attractive', 'awful', 'awestruck', 'beautiful', 'chilly', 'bashful', 'bold', 
  'depressed', 'cautious', 'brave', 'dirty', 'composed', 'cheerful', 'dreadful', 'easygoing', 'comfortable', 'heavy', 'horrified', 
  'delightful', 'irritated', 'intelligent', 'excited', 'pessimistic', 'mysterious', 'festive', 'tearful', 'political', 'free', 'tense', 
  'quizzical', 'jolly', 'terrible', 'religious', 'optimistic', 'tired', 'secretive', 'proud', 'ugly', 'secular', 'wonderful', 'weak', 
  'shy', 'appreciative', 'angry', 'accepting', 'blissful', 'disenchanted', 'calm', 'contented', 'distressed', 'confident', 'ecstatic', 
  'glum', 'cool', 'elated', 'gloomy', 'earnest', 'glad', 'grumpy', 'easy', 'happy', 'grouchy', 'evenhanded', 'joyful', 'miserable', 
  'indifferent', 'jubilant', 'mad', 'neutral', 'merry', 'moody', 'nonpartisan', 'respectful', 'nervous', 'passive', 'sweet', 'sad', 
  'reserved', 'serene', 'sadistic', 'satisfied', 'upbeat', 'selfish', 'surprised', 'vivacious', 'sour', 'tranquil'
]

questions = {
    "i want": "why do you want ",
    "i feel": "what makes you feel",
    "i think": "what makes you think",
    "i believe in": "interesting belief, why do you believe",
    "i need": "would it really help you to get",
    "i can't": "what do you think is the reason you can't",
    "are you": "Why do you care if i am",
}

commonAnswers = {
    "no": "Why not?",
    "sorry" : "No need for apologies.",
    "maybe": "You dont seem certain about that.",
    "perhaps": "Why the uncertain tone?",
    "name": "I dont care for names",
    "i was": "Oh interesting. Were you really?"
}

reflections = {
  "was": "were",
  "am": "are",
  "i": "you",
  "im": "you are",
  "we" : "you",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "i will": "you will",
  "my": "your", #
  "are": "am",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me", #
  "me": "you"
}

default_answers = ['Hmmm... Tell me more', 'Oh really, why exactly?', 'Can you elaborate on that?', 'You should probably talk to me about that', 'Go on, I am listening...']

confused = ["i have no idea what you're talking about...", "maybe try saying something simpler?", 
                    "sorry i don't understand, try saying something else", "i'm not smart enough to answer that sorry"]

if __name__ == '__main__':
    Main()