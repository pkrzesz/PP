import random
random.seed()

# do zrobienia:
# dodanie komentarzy w poprawne miejsca, aby opisać które wymagania są spełniane przez jaką część kodu 
# (klasa pytanie jest globalna złożona na przykład, a liczby a, b, x i y w funkcji gra() to lokalne proste)
# faktyczne dodanie faktycznych pytań i zwiększenie ich ilości

# komentarz do osoby to widzącej:
# dict (mapa), oraz tuple (tupla) zostały praktycznie użyte jako list (lista)

def gra():
    a = 0
    b = 0
    for key in range(12):
        lista = dictoflists[key]
        x = random.randint(0, len(lista)-1)
        lista[x].print()
        print("Pytanie numer", key)
        y = odpowiedz(lista[x])
        if y == "INCORRECT" or y == "END":
            break
        else:
            print("Poprawna odpowiedz")
            a+=1
            if money[a] in guaranteedmoney:
                b+=1
                print("Masz teraz gwarantowane", guaranteedmoney[b], "PLN")
    if y == "INCORRECT":
        print("Niestety, poprawna odpowiedz byla", lista[x].correct)
        print("Wygrales", guaranteedmoney[b], "PLN")
    else:
        print("Wygrales", money[a], "PLN")
    ponownie(y)

def odpowiedz(lista):
    answer = input("Jaka jest twoja odpowiedz?\nWpisz a, b, c, d lub stop aby zakończyć grę wcześnie\n")
    if answer.lower() == lista.correct:
        return "CORRECT"
    elif answer.lower() in ["a", "b", "c", "d"]:
        return "INCORRECT"
    elif answer.lower() == "stop":
        return "END"
    else:
        print("Odpowiedz z poza zakresu przyjmowanych odpowiedzi, sproboj ponownie")
        return odpowiedz(lista)
    
def ponownie(wynik):
    if wynik == "END":
        again = wynik
    else:
        again = input("Zagrasz ponownie?(y/n)\n").lower()
    match again:
        case "END":
            print("Gra zakonczona komenda stop")
        case "y":
            print("Zagrajmy ponownie, przed tobą 12 pytań")
            gra()
        case "n":
            print("Dziekujemy za gre")
        case _:
            print("Odpowiedz poza zakresem")
            ponownie(wynik)

            
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
        print("a:", self.a)
        print("b:", self.b)
        print("c:", self.c)
        print("d:", self.d)

money = (0, 500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000)
guaranteedmoney = (0, 1000, 40000, 1000000)
dictoflists = {0:[pytanie("test?", "A", "b", "c", "d", "a"),
                pytanie("test?", "a", "B", "c", "d", "b"),
                pytanie("test?", "a", "b", "C", "d", "c"),
                pytanie("test?", "a", "b", "c", "D", "d")],
               1:[pytanie("test1?", "1A", "b", "c", "d", "a"),
                pytanie("test1?", "a", "1B", "c", "d", "b"),
                pytanie("test1?", "a", "b", "1C", "d", "c")],
               2:[pytanie("test2?", "2A", "b", "c", "d", "a"),
                  pytanie("test2?", "a", "2B", "c", "d", "b"),
                  pytanie("test2?", "a", "b", "2C", "d", "c"),
                  pytanie("test2?", "a", "b", "c", "2D", "d"),
                  pytanie("test2?", "no", "nope", "this one", "nah", "c")],
               3:[pytanie("test3?", "alpha", "bravo", "CHARLIE", "delta", "c")]}

print("Witamy w milionerach, przed toba 12 pytan")
gra()