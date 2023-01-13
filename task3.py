# Dominik Borawski
# A1 215IC
#############
# ZADANIE 3 #
#############
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
#generuje 200 probek skupionych wokol 4 centrow - ponownie, niepotrzebna zadna petla ani nawet dwie.
X, _ = make_blobs(n_samples=200, centers=4)
#tworze nowy obiekt KMeans, zaznaczam w konstruktorze ze maja byc 4 centra
kmeans = KMeans(4)
#przypisuje wygenerowane punkty do "bazy" utworzonego obiektu kmeans, na ich podstawie beda wykonywane dalsze operacje
kmeans.fit(X)
#znajduje optymalne centra
#w jednej linijce wykonywana jest logika ktora w recznym kodzie zajmuje zdecydowanie wiecej
y = kmeans.predict(X)
#zapisuje je do zmiennej
Centers = kmeans.cluster_centers_
#umieszczam na wykresie punkty (bardzo przyjazne operacje na listach []).
plt.scatter(X[:, 0], X[:,1], s=30, c=y)
#umieszczam na wykresie centra i wyswietlam wykres
plt.scatter(Centers[0][0], Centers[0][1], c="purple", s=100, marker="s",edgecolors="black")
plt.scatter(Centers[1][0], Centers[1][1], color="steelblue", s=100, marker="s", edgecolors="black")
plt.scatter(Centers[2][0], Centers[2][1], color="mediumseagreen", s=100, marker="s", edgecolors="black")
plt.scatter(Centers[3][0], Centers[3][1], color="yellow", s=100, marker="s", edgecolors="black")
plt.show()

