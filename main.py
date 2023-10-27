import random
random.seed()

def gra():
    a = 0
    b = 0
    for key in money:
        while key < 1000000:
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
        if y == "INCORRECT" or y == "END":
            break
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
dictoflists={
                0:[pytanie("test?", "A", "b", "c", "d", "a"),
                pytanie("test?", "a", "B", "c", "d", "b"),
                pytanie("test?", "a", "b", "C", "d", "c"),
                pytanie("test?", "a", "b", "c", "D", "d")],
                500:[pytanie("test1?", "1A", "b", "c", "d", "a"),
                pytanie("test1?", "a", "1B", "c", "d", "b"),
                pytanie("test1?", "a", "b", "1C", "d", "c"),
                pytanie("test1?", "a", "b", "c", "1D", "d")],
                1000:[pytanie("test2?", "2A", "b", "c", "d", "a"),
                  pytanie("test2?", "a", "2B", "c", "d", "b"),
                  pytanie("test2?", "a", "b", "2C", "d", "c"),
                  pytanie("test2?", "a", "b", "c", "2D", "d")],
                2000:[pytanie("test3?", "3A", "b", "c", "d", "a"),
                  pytanie("test3?", "a", "3B", "c", "d", "b"),
                  pytanie("test3?", "a", "b", "3C", "d", "c"),
                  pytanie("test3?", "a", "b", "c", "3D", "d")],
                5000:[pytanie("test4?", "4A", "b", "c", "d", "a"),
                pytanie("test4?", "a", "4B", "c", "d", "b"),
                pytanie("test4?", "a", "b", "4C", "d", "c"),
                pytanie("test4?", "a", "b", "c", "4D", "d")],
                10000:[pytanie("test?5", "5A", "b", "c", "d", "a"),
                pytanie("test5?", "a", "5B", "c", "d", "b"),
                pytanie("test5?", "a", "b", "5C", "d", "c"),
                pytanie("test5?", "a", "b", "c", "5D", "d")],
                20000:[pytanie("test6?", "6A", "b", "c", "d", "a"),
                pytanie("test6?", "a", "6B", "c", "d", "b"),
                pytanie("test6?", "a", "b", "6C", "d", "c"),
                pytanie("test6?", "a", "b", "c", "6D", "d")],
                40000:[pytanie("test7?", "7A", "b", "c", "d", "a"),
                pytanie("test7?", "a", "7B", "c", "d", "b"),
                pytanie("test7?", "a", "b", "7C", "d", "c"),
                pytanie("test7?", "a", "b", "c", "7D", "d")],
                75000:[pytanie("test8?", "8A", "b", "c", "d", "a"),
                pytanie("test8?", "a", "8B", "c", "d", "b"),
                pytanie("test8?", "a", "b", "8C", "d", "c"),
                pytanie("test8?", "a", "b", "c", "8D", "d")],
                125000:[pytanie("test9?", "9A", "b", "c", "d", "a"),
                pytanie("test9?", "a", "9B", "c", "d", "b"),
                pytanie("test9?", "a", "b", "9C", "d", "c"),
                pytanie("test9?", "a", "b", "c", "9D", "d")],
                250000:[pytanie("test10?", "10A", "b", "c", "d", "a"),
                pytanie("test10?", "a", "10B", "c", "d", "b"),
                pytanie("test10?", "a", "b", "10C", "d", "c"),
                pytanie("test10?", "a", "b", "c", "10D", "d")],
                500000:[pytanie("test11?", "11A", "b", "c", "d", "a"),
                pytanie("test11?", "a", "11B", "c", "d", "b"),
                pytanie("test11?", "a", "b", "11C", "d", "c"),
                pytanie("test11?", "a", "b", "c", "11D", "d")]
                }

print("Witamy w milionerach, przed toba 12 pytan")
gra()