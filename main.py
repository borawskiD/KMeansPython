# Dominik Borawski
# A1 215IC
#############
# ZADANIE 3 #
#############


import random
import math
from matplotlib import pyplot as plt


# zadanie 1 (niektórych funkcji używam też do zadania 2

# funkcja do generowania okreslonej ilości pary punktów (x,y). Po wygenerowaniu zwracam w formie listy.
def generatePoints(size):
    points = [[random.random(), random.random()]]
    for i in range(size - 1):
        points.append([random.random(), random.random()])
    return points


# funkcja do liczenia euklidesowej odleglosci, prosta implementacja wzoru zalaczonego w skrypcie.
def d(A, B):
    return math.sqrt(math.pow((A[0] - B[0]), 2) + math.pow((A[1] - B[1]), 2))


# funkcja do filtracji dystansow do okreslonych centrów;
# analizuje wszystkie cztery dystanse, a nastepnie szukam najmniejszej i zwracam w formie listy [x,y,[x_c,y_c]].
def findTheBestDistance(point, clasters):
    distanceToClasters = [d(point, clasters[0]), d(point, clasters[1]), d(point, clasters[2]), d(point, clasters[3])]
    print("\n")
    for x in distanceToClasters:
        print(x)
    return [point[0], point[1], distanceToClasters.index(min(distanceToClasters))]


# obudowa do funkcji znajdujacej klastry, ktora ma na celu po prostu wykonanie funkcji do wszystkich punktow w klasie
# z jakiegos powodu inicjalizacja pustej listy w pythonie niekoniecznie chce ze mna wspolpracowac - musze najpierw
# recznie zainicjowac z 1-szym punktem, a potem go omijac, inaczej indeksacja zaczyna sie od 1. elementu a 0 jest pusty.
def findTheRightClasters(points, clasters):
    pointsWithClasters = [findTheBestDistance(points[0], clasters)]
    print(len(pointsWithClasters))
    for x in points:
        if points.index(x) == 0:
            continue
        pointsWithClasters.append(findTheBestDistance(x, clasters))
    return pointsWithClasters


# tutaj funkcja do printowania wynikow, zlicza ilosc wystapien okreslonej liczby oznaczajacej konkretne centrum
# a potem dzieli przez wszystkie i wylicza procent.
# autorefleksja - w javie zajeloby to troche wiecej kodu, bardzo przydatne sa te metody wbudowane.
def countOccurances(point):
    print("Ilosc punktow dla centra klasy numer 0: " + str(sum([row.count(0) for row in point])) + " [" + str(
        round((sum([row.count(0) for row in point]) / 400) * 100)) + "%]")
    print("Ilosc punktow dla centra klasy numer 1: " + str(sum([row.count(1) for row in point])) + " [" + str(
        round((sum([row.count(1) for row in point]) / 400) * 100)) + "%]")
    print("Ilosc punktow dla centra klasy numer 2: " + str(sum([row.count(2) for row in point])) + " [" + str(
        round((sum([row.count(2) for row in point]) / 400) * 100)) + "%]")
    print("Ilosc punktow dla centra klasy numer 3: " + str(sum([row.count(3) for row in point])) + " [" + str(
        round((sum([row.count(3) for row in point]) / 400) * 100)) + "%]")


# wlasciwy kod algorytmu.
# 1. generacja 400 punktow
# 2. generacja 4 centrow
# 3. znalezienie najlepszych centrow dla kazdego z punktow
# 4. policzenie wystapien
# 5. narysowanie wykresu
def taskOne():
    points = generatePoints(400)
    clasters = generatePoints(4)
    findTheBestDistance(points[1], clasters)
    pointsWithClasters = findTheRightClasters(points, clasters)
    countOccurances(pointsWithClasters)
    drawGraph(pointsWithClasters, clasters)


# odpowiedni kod do uruchamiania - zakomentowany, poniewaz w tym pliku realizuje rowniez 2. zadanie
# (jak przeszedlem do 3. to okazalo sie to glupim pomyslem, ponieważ 3. zrelizowałem w 10% ilosci linijek kodu co 2 poprzednie).

# taskOne()
# plt.show()
# proste nanoszenie danych na wykres, centra sa troche wieksze niz pozostale punkty.
def drawGraph(pointsWithClasters, clasters):
    plt.scatter(clasters[0][0], clasters[0][1], color="blue", s=300)
    plt.scatter(clasters[1][0], clasters[1][1], color="green", s=300)
    plt.scatter(clasters[2][0], clasters[2][1], color="purple", s=300)
    plt.scatter(clasters[3][0], clasters[3][1], color="red", s=300)
    for pointLabel in pointsWithClasters:
        if pointLabel[2] == 0:
            plt.scatter(pointLabel[0], pointLabel[1], color="blue")
        if pointLabel[2] == 1:
            plt.scatter(pointLabel[0], pointLabel[1], color="green")
        if pointLabel[2] == 2:
            plt.scatter(pointLabel[0], pointLabel[1], color="purple")
        if pointLabel[2] == 3:
            plt.scatter(pointLabel[0], pointLabel[1], color="red")


#############
# ZADANIE 2 #
#############
# tutaj jedna z istotniejszych funkcji, ktora na pewno moglaby byc krotsza korzystajac z metod wbudowanych
# licze srednia z punktow w poszczegolnych centrach zeby wyznaczyc nowe centrum, optymalniejsze.
def findAverage(points, label):
    num = 0
    xValue = 0
    yValue = 0
    for pointLabel in points:
        if pointLabel[2] == label:
            num += 1
            xValue += pointLabel[0]
            yValue += pointLabel[1]

    return [xValue / num, yValue / num]


# warunek konczacy petle, gdy nie ma przesuniecia zadnego z 4. centrow to nie ma sensu dalej iterowac
def foundPerfectCenter(differences):
    return differences[0] == 0.0 and differences[1] == 0.0 and differences[2] == 0.0 and differences[3] == 0.0


# glowna metoda drugiego zadania. algorytm w kolejnych krokach:
# 1. generacja 200 punktow
# 2. generacja 4 centrow
# 3. naniesienie centrow na wykres
# 4. skorzystanie z metody z 1. zadania do znalezienia optymalnych centrow
# 5. petla do-while w ktorej:
#     wykonuje kopie starych centrow
#     znajduje srednie dla kazdego z klastrow (zgodnie z komentarzem do metody)
#     wyliczam roznice miedzy starymi a nowymi centrami
#     jesli jest rozna od zera to kontynuuje
# a na koniec rysuje wykres.

def taskTwo():
    points = generatePoints(200)
    clasters = generatePoints(4)
    points = findTheRightClasters(points, clasters)
    while True:
        oldClasters = clasters.copy()
        clasters = [findAverage(points, 0), findAverage(points, 1), findAverage(points, 2), findAverage(points, 3)]
        differences = [d(clasters[0], oldClasters[0]), d(clasters[1], oldClasters[1]), d(clasters[2], oldClasters[2]),
                       d(clasters[3], oldClasters[3])]
        print("roznica = " + str(differences))
        if foundPerfectCenter(differences):
            break
    drawGraph(points, clasters)


taskTwo()
plt.show()
