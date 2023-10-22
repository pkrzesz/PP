import random
random.seed()

def odpowiedz(lista):
    answer = input("What is your answer?\n")
    if answer.lower() == lista.correct:
        return "CORRECT"
    elif answer.lower() in ["a", "b", "c", "d"]:
        return "INCORRECT"
    else:
        print("Answer outside of range, try again")
        return odpowiedz(lista)

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

listoflists = [[pytanie("test?", "A", "b", "c", "d", "a"),
                pytanie("test?", "a", "B", "c", "d", "b"),
                pytanie("test?", "a", "b", "C", "d", "c"),
                pytanie("test?", "a", "b", "c", "D", "d")],
               [pytanie("test2a?", "2A", "b", "c", "d", "a"),
                pytanie("test2b?", "a", "2B", "c", "d", "b")]]

for list in listoflists:
    x = random.randint(0, len(list)-1)
    list[x].print()
    y = odpowiedz(list[x])
    print(y)
    if y == "INCORRECT":
        break