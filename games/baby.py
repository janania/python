#Baby Simulator
from random import choice
questions = ["Why does the beach have waves?: ",
             "Where are the dinosaurs?: ",
             "Where did humans come from?: ",
             "Why are plants green?: "]

questions = choice(questions)
answer = input(questions).strip().lower()

while answer != "just because":
    answer = input("Why? ")

print("Oh..Ok")

