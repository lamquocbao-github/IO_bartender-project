# import pandas as pd
import random

questions = {
 "strong": "Do ye like yer drinks strong?",
 "salty": "Do ye like it with a salty tang?",
 "bitter": "Are ye a lubber who likes it bitter?",
 "sweet": "Would ye like a bit of sweetness with yer poison?",
 "fruity": "Are ye one for a fruity finish?"}

ingredients = {
 "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

# function to make random quest
def rand_quest(quest):
    topic = list(quest.keys())
    rand_topic = random.sample(topic,len(topic))
    return rand_topic
random_quest = rand_quest(questions)
# print(random_quest)
# start io
i = input("Do you want to get something to drink?")
if i.upper() == "Y" or i.upper() == "YES":
    for l in range(0, len(questions)):
        q_topic = random_quest[l]
        q = input(questions[q_topic] + " (y/n)")
        if q.upper() == "Y" or q.upper() == "YES":
            a_rand = random.sample(ingredients[q_topic],1)[0]
            print("Enjoy your drink: " + a_rand + "!")
            break
        elif q.upper() == "N" or q.upper() == "NO":
            if l == int(len(questions)-1):
                print("Drink can't be found!")
                break
else: print("See you next time!")
