import random
random.seed()

class pytanie:
    def __init__(self, question, a, b, c, d, correct):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct
    
    def print(self):
        print(self.question)
        print(self.a, self.b)
        print(self.c, self.d)

list = [pytanie("test?", "A", "b", "c", "d", "a"), pytanie("test?", "a", "B", "c", "d", "b"), pytanie("test?", "a", "b", "C", "d", "c"), pytanie("test?", "a", "b", "c", "D", "d")]

x = random.randint(0, len(list)-1)

list[x].print()
def odpowiedz(lista, x):
    answer = input("What is your answer?\n")
    if answer.lower() == lista[x].correct:
        print("CORRECT")
    elif answer.lower() in ["a", "b", "c", "d"]:
        print("INCORRECT")
    else:
        print("Answer outside of range, try again")
        odpowiedz(lista, x)

odpowiedz(list, x)