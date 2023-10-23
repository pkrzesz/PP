import random
random.seed()

def odpowiedz(lista):
    answer = input("What is your answer?\nType in a, b, c or d, or end the game early with stop\n")
    if answer.lower() == lista.correct:
        return "CORRECT"
    elif answer.lower() in ["a", "b", "c", "d"]:
        return "INCORRECT"
    elif answer.lower() == "stop":
        return "END"
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

money = (0, 500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000)
guaranteedmoney = (0, 1000, 40000, 1000000)
listoflists = [[pytanie("test?", "A", "b", "c", "d", "a"),
                pytanie("test?", "a", "B", "c", "d", "b"),
                pytanie("test?", "a", "b", "C", "d", "c"),
                pytanie("test?", "a", "b", "c", "D", "d")],
               [pytanie("test2a?", "2A", "b", "c", "d", "a"),
                pytanie("test2b?", "a", "2B", "c", "d", "b")],[pytanie("test3?", "a", "b", "c", "D", "d")],[pytanie("test4?", "alpha", "bravo", "CHARLIE", "delta", "c")]]
a = 0
b = 0
for list in listoflists:
    x = random.randint(0, len(list)-1)
    list[x].print()
    y = odpowiedz(list[x])
    print(y)
    if y == "INCORRECT" or y == "END":
        break
    else:
        a+=1
        if money[a] in guaranteedmoney:
            b+=1
if y == "INCORRECT":
    print("Wygrales ", guaranteedmoney[b], "PLN")
else:
    print("Wygrales ", money[a], "PLN")