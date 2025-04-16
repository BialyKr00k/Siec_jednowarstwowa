Projekt 3 NAI - sieć jednowarstwowa:

>>> def funkcja_aktywacji(suma):
jeśli suma >= 0 to zwraca +1, jeśli suma < 0 to -1
Funkcja decyzyjna perceptronu - podejmuje binarną decyzję

Input: 
liczba typu float

Output: 
+1 lub -1

>>> def funkcja_wejścia(wagi, x):
iloczyn skalarny wag i wektora cech: suma = w1*x1 + … + wn * xn
Mierzy jak bardzo dana próbka "pasuje" do wzorca (wag)
Wzorzec (hiperpowierzchnia -> suma w*x) mówi, po której stronie granicy znajduje
się próbka

1. lista wag [0.1, 0.2, 0.3] (float)
2. x - lista floatów (wektor cech - obliczony przez def wylicz_wektor_cech())
3. suma - przechowuje wynik iloczynu skalarnego
3. zip(wagi, x) -> połączenie list wag i wartości cech
4. dla każdej pary mnożymy wagę razy wartość cechy i dodajemy do sumy
5. zwracamy sumę -> dowód jak bardzo dane wejście pasuje do modelu

Output:
suma - liczba float

>>> def norm_wektora(wektor):
normalizacja wektora (skraca wektor do długości 1) - normalizacja do długości jednostkowej
oblicza długość wektora (norma)
dzieli każdy element przez normę -> wynikowy wektor długość 1
Zapewnia, że różnice w długości tekstu nie wpływaja na klasyfikację
Zatem umożliwia uczciwe porównanie tekstów o różnej długości

1. wektor - lista floatów 

Output:
wektor o tej samej liczbie elementów, ale długości 1

np.: [3, 4] -> [0.6, 0.8]

>>> def wylicz_wektor_cech(tekst):
zamienia tekst na wektor cech oparty na częstości liter a-z
1.usuwa znaki niebędące literami
2.zlicza wystąpienia każdej litery a-z
3.dzieli przez długość -> daje częstość liter
4.normalizuje ten wektor do długości 1
Zamienia tekst na liczbowy wektor cech, który perceptron może analizować
Perceptron nie rozumie słów, tylko liczby, więc trzeba przekształcić tekst na liczby
opisujące jego strukturę

Input:
tekst - string

Output:
lista 26 floatów (częstości liter a-z) - znormalizowana

>>> def trening(l1, l2, a, epoki=1000):
uczy jeden perceptron dla problemu binaryfikowanego (-1 vs +1)
1.Tworzy listę wag (na start same 0)
2.w każdej epoce dla każdego przykładu oblicza predykcję, jeśli błąd -> aktualizuje wagi
3.Normalizuje wagi
Wagi są korygowane na podstawie błędów
Algorytm oparty na zasadzie minimalizacji błędów klasyfikacji

Input:
l1 - lista wektorów cech (lista floatów)
l2 - lista etykiet +1 lub -1
a - stała uczenia (float)
epoki - ilość iteracji przez dane (int)

Output:
lista wag znormalizowana (float)

>>> def zaladuj_dane(trening_files):
wczytuje teksty z plików, przelicza je na wektory cech
1.Dla każdego języka: otwiera pliki, wczytuje tekst, tworzy wektor cech
2.Zapisuje wszystko w słowniku dane
Przygotowuje dane treningowe dla perceptronu

Input: 
trening_files - słownik {język : [plik1, ...]

Output:
słownik - {język : [wektor_cech, ...]

>>> def trening perceptronów(dane, a=0.1, epoki=1000):
tworzy jeden perceptron dla każdego języka
1.Buduje listę wszystkich wektorów + ich etykiety
2.Dla każdego języka przygotowuje etykiety +1 (ten język) i -1 (inny język), trenuje perceptron,
zapisuje wagi do słownika
Trzeba nauczyć perceptron rozpoznawać każdy język - oddzielnie
Klasyfikacja wieloklasowa zbudowana z wielu binarnych - 1 vs rest

>>> def klasyfikuj_tekst(tekst, perceptrony)
Klasyfikuje podany tekst - sprawdza, który perceptron daje najwyższy wynik
1.Tworzy wektor cech z tekstu
2.Dla każdego języka oblicza iloczyn wag i wektora
3.Wybiera język z największym wynikiem
Główny etap klasyfikacji -> przypisanie nowego tekstu do jednej z klas
Największy iloczyn wag i cech = największa pewność, że tekst należy do tej klasy

Input:
teskt - string (zdanie do klasyfikacji)
perceptrony - słownik {język : wagi}

Output:
wybrany_język - string (nazwa języka z najwyższym wynikiem)
wyniki - słownik {język : wynik(float)}

>>> def main():
1.słownik - dla każdego języka przypisana jest lista plików .txt z tekstami
2.def zaladuj_dane()
3.Jeśli def zaladuj_dane() nie wczytało żadnych danych, program kończy działanie
4.def trening_perceptronów() - dla każdego języka tworzony jest osobny perceptron
trenujący się w systemie 1 vs reszta, zwracany jest słownik:
perceptrony = {
	"polski" : [wagi_polskiego]
	"slowacki" : [wagi_slowackiego]
	"czeski" : [wagi_czeskiego]
}
5.Pętla do klasyfikacji inputu użytkownika
6.Użytkownik podaje jakiś tekst/zdanie/wyrazenie, ENTER -> WYJŚCIE
7.def klasyfikuj_tekst(wejscie, perceptrony) -> przelicza tekst na wektor cech,
dla każdego języka obliczana jest wartość aktywacji (iloczyn skalarny wag i wektora)
Zwraca:
język -> język z najwyższym wynikiem
wyniki -> słownik {język : wynik}
