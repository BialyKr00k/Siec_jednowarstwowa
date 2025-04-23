Sieć jednowarstwowa:

def funkcja_aktywacji(suma):
- jeśli suma >= 0 to zwraca +1, jeśli suma < 0 to -1
- Funkcja decyzyjna perceptronu - podejmuje binarną decyzję
- Input: 
liczba typu float
- Output: 
+1 lub -1

def funkcja_wejścia(wagi, x):
- iloczyn skalarny wag i wektora cech: suma = w1*x1 + … + wn * xn
- mierzy jak bardzo dana próbka "pasuje" do wzorca (wag)
- wzorzec (hiperpowierzchnia -> suma w*x) mówi, po której stronie granicy znajduje się próbka

1. lista wag [0.1, 0.2, 0.3] (float)
2. x - lista floatów (wektor cech - obliczony przez def wylicz_wektor_cech())
3. suma - przechowuje wynik iloczynu skalarnego
3. zip(wagi, x) -> połączenie list wag i wartości cech
4. dla każdej pary mnożymy wagę razy wartość cechy i dodajemy do sumy
5. zwracamy sumę -> dowód jak bardzo dane wejście pasuje do modelu

- Output: 
suma - liczba float

def norm_wektora(wektor):
- normalizacja wektora (skraca wektor do długości 1) - normalizacja do długości jednostkowej oblicza długość wektora (norma)
- dzieli każdy element przez normę -> wynikowy wektor długość 1
- zapewnia, że różnice w długości tekstu nie wpływaja na klasyfikację
- zatem umożliwia uczciwe porównanie tekstów o różnej długości

1. wektor - lista floatów
2. norma - norma euklidesowa (długość wektora)
3. jeśli wektor to 0, to nie da się go znormalizować -> zwrot oryginalnego wektora
4. dzielimy każdy element wektora przez jego długość np.: [3, 4] -> norma = 5 -> res = [0.6, 0.8]

- Output:
wektor o tej samej liczbie elementów, ale długości 1
np.: [3, 4] -> [0.6, 0.8]

def wylicz_wektor_cech(tekst):
- zamienia tekst na wektor cech oparty na częstości liter a-z
- usuwa znaki niebędące literami
- zlicza wystąpienia każdej litery a-z
- dzieli przez długość -> daje częstość liter
- normalizuje ten wektor do długości 1
- pamienia tekst na liczbowy wektor cech, który perceptron może analizować
- perceptron nie rozumie słów, tylko liczby, więc trzeba przekształcić tekst na liczby opisujące jego strukturę

1. tekst - string
2. cały tekst na małe litery
3. dozwolone - zbiór 26 liter alfabetu łacińskiego a-z
4. flitered - lista tylko tych znaków, które są literami a-z
5. suma_liter - zlicza ile liter w sumie znajduje się w tekście po odfiltrowaniu (do obliczenia procentowgo udziału)
6. wektor z 26 zerami -> dla każdej litery
7. aby uniknąć dzielenia przez 0 przy normalizacji to zwracamy wektor zer (jesli nie ma żadnych liter)
8. Zliczamy ile razy pojawiła się każda litera
9. każdą wartość w wektorze dzielimy przez sumę liter -> częstość występowania każdej litery (proporcja)

- Output:
zwraca znormalizowany wektor cech (długość = 1), aby długości tekstu nie miały wpływu na wynik 

def trening(l1, l2, a, epoki=1000):
- uczy jeden perceptron dla problemu binaryfikowanego (-1 vs +1)

1. Dane, które wchodzą do funkcji:
l1 - lista wektorów cech (lista floatów)
l2 - lista etykiet +1 lub -1
a - stała uczenia (float)
epoki - ilość iteracji przez dane (int)
2. liczba_cech - oblicza ile cech ma pojedynczy wektor (długość jednego wektora cech)
potrzebujemy dokładnie tyle wag ile jest cech
3. Tworzymy listę wag o długości 26 (liczba cech), na początku wszystkie wagi = 0
Potrzebujemy jej do nauki perceptronu poprzez modyfikację wag
4. Pętla iterująca poprzez zbiór treningowy tyle razy ile jest epok - perceptron
może potrzebować wielu przejść, żeby poprawnie nauczyć się rozróżniać klasy
5. Pętla iterująca po wszystkich przykładach treningowych: 
xi - wektor cech, do którego przypisujemy aktualny wektor cech -> l1[i]
6. suma - iloczyn skalarny -> obliczenie aktywacji neuronu
7. przew_et - do której klasy został przypisany przykład (-1 lub +1)
8. blad - jeśli perceptron się pomylił to trzeba zmodyfikować wagi,
jeśli blad = 0 - jest dobrze
9. Korekcja wag

- Output:
lista wag znormalizowana (float), 

def zaladuj_dane(trening_files):
- wczytuje teksty z plików, przelicza je na wektory cech
1.Dla każdego języka: otwiera pliki, wczytuje tekst, tworzy wektor cech
2.Zapisuje wszystko w słowniku dane
- przygotowuje dane treningowe dla perceptronu

- Input: 
trening_files - słownik {język : [plik1, ...]

- Output:
słownik - {język : [wektor_cech, ...]

def trening_perceptronów(dane, a=0.1, epoki=1000):
- tworzy jeden perceptron dla każdego języka
1. Dane, które wchodzą do funkcji:
dane - słownik {język : lista wektorów cech}
a - stała uczenia perceptronu
epoki - liczba iteracji
2. jezyki - pobieramy listę języków, bedziemy trenować osobny perceptron dla każdego języka
3. wszystkie_teksty - lista wszystkich wektorów cech
etykiety_globlane - odpowiadające im etykiety - języki 
ułatwia to późniejsze tworzenie etykiet binarnych dla każdego perceptronu
4. pętla for - dla każdgo języka i wektora cech dodajemy go do listy wszystkie_teksty,
zapisujemy jego etykietę (język) w etykiety_globalne
5. perceptrony - słownik, do którego zapisujemy wagi dla każdego języka
6. pętla for - pętla po językach - język X -> +1, inny -> -1
7. l1 - lista wektora cech (dane wejściowe). l2 - lista etykiet binarnych dla perceptronu
8. pętla for - +1 jeśli język pasuje do aktualnie trenowanego perceptronu, -1 dla pozostałych języków
9. wagi - uruchamiamy def trening() - zwraca nauczone wagi perceptronu dla danego języka
10. perceptrony[jezyk_docelowy] - zapisujemy wagi do słownika pod kluczem danego języka

Output:
gotowe perceptrony (zbiory wag) dla każdego języka

def klasyfikuj_tekst(tekst, perceptrony)
- klasyfikuje podany tekst - sprawdza, który perceptron daje najwyższy wynik
- celem jest zamienienie tekstu na wektor cech, porównać go z każdym perceptronem i zdecydować, 
do którego języka najbardziej pasuje

1. Dane, które wchodzą do funkcji:
teskt - tekst wpisany przez użytkownika
perceptrony - słownik z wagami wytrenowanych perceptronów dla każdego języka
2. wektor - def wylicz_wektor_cech() - przekształca tekst na czysty wektor długości 26,
znormalizowany do długości 1 - matematyczna reprezentacja tekstu
3. wyniki - wyniki aktywacji perceptronu dla każdego języka
4. pętla for - iterujemy po każdym języku i jego perceptronie

- Input:
teskt - string (zdanie do klasyfikacji)
perceptrony - słownik {język : wagi}

- Output:
wybrany_język - string (nazwa języka z najwyższym wynikiem)
wyniki - słownik {język : wynik(float)}

def main():
1. słownik - dla każdego języka przypisana jest lista plików .txt z tekstami
2. def zaladuj_dane()
3. jeśli def zaladuj_dane() nie wczytało żadnych danych, program kończy działanie
4. def trening_perceptronów() - dla każdego języka tworzony jest osobny perceptron
trenujący się w systemie 1 vs reszta, zwracany jest słownik:
perceptrony = {
	"polski" : [wagi_polskiego]
	"slowacki" : [wagi_slowackiego]
	"czeski" : [wagi_czeskiego]
}
5. Pętla do klasyfikacji inputu użytkownika
6. Użytkownik podaje jakiś tekst/zdanie/wyrazenie, ENTER -> WYJŚCIE
7. def klasyfikuj_tekst(wejscie, perceptrony) -> przelicza tekst na wektor cech,
dla każdego języka obliczana jest wartość aktywacji (iloczyn skalarny wag i wektora)
Zwraca:
język -> język z najwyższym wynikiem
wyniki -> słownik {język : wynik}
