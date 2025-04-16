import string
import math

def funkcja_aktywacji(suma):
    return +1 if suma >= 0 else -1

def funkcja_wejscia(wagi, x):
    suma = 0.0
    for w, xi in zip(wagi, x):
        suma += w * xi
    return suma

def norm_wektora(wektor):
    norma = math.sqrt(sum(x * x for x in wektor))
    if norma == 0:
        return wektor
    return [x / norma for x in wektor]

def wylicz_wektor_cech(tekst):
    tekst = tekst.lower()
    dozwolone = set(string.ascii_lowercase)
    filtered = [c for c in tekst if c in dozwolone]
    suma_liter = len(filtered)

    wektor = [0] * 26
    if suma_liter == 0:
        return wektor

    for litera in filtered:
        index = ord(litera) - ord('a')
        if 0 <= index < 26:
            wektor[index] += 1

    wektor = [count / suma_liter for count in wektor]
    return norm_wektora(wektor)

def trening(l1, l2, a, epoki=1000):
    liczba_cech = len(l1[0])
    wagi = [0.0] * liczba_cech

    for _ in range(epoki):
        for i in range(len(l1)):
            xi = l1[i]
            suma = funkcja_wejscia(wagi, xi)
            przew_et = funkcja_aktywacji(suma)
            blad = l2[i] - przew_et
            if blad != 0:
                for j in range(liczba_cech):
                    wagi[j] += a * l2[i] * xi[j]
    return norm_wektora(wagi)

def zaladuj_dane(training_files):
    dane = {}

    for jezyk, lista_plikow in training_files.items():
        teksty = []

        for sciezka in lista_plikow:
            try:
                with open(sciezka, 'r', encoding='utf-8') as x:
                    tekst = x.read()
                    wektor = wylicz_wektor_cech(tekst)
                    teksty.append(wektor)
            except Exception as e:
                print(f"Błąd przy wczytywaniu pliku {sciezka}: {e}")
        if teksty:
            dane[jezyk] = teksty
    return dane

def trening_perceptronow(dane, a=0.1, epoki=1000):
    jezyki = list(dane.keys())
    wszystkie_teksty = []
    etykiety_globalne = []

    for jezyk in jezyki:
        for wektor in dane[jezyk]:
            wszystkie_teksty.append(wektor)
            etykiety_globalne.append(jezyk)

    perceptrony = {}

    for jezyk_docelowy in jezyki:
        l1 = []
        l2 = []

        for wektor, etykieta in zip(wszystkie_teksty, etykiety_globalne):
            l1.append(wektor)
            l2.append(+1 if etykieta == jezyk_docelowy else -1)
        print(f"Trening perceptronu dla języka: {jezyk_docelowy}")
        wagi = trening(l1, l2, a, epoki)
        perceptrony[jezyk_docelowy] = wagi

    return perceptrony

def klasyfikuj_tekst(tekst, perceptrony):
    wektor = wylicz_wektor_cech(tekst)
    wyniki = {}

    for jezyk, wagi in perceptrony.items():
        suma = funkcja_wejscia(wagi, wektor)
        wyniki[jezyk] = suma

    wybrany_jezyk = max(wyniki, key=wyniki.get)

    return wybrany_jezyk, wyniki

def main():
    training_files = {
        "polski": [
            "1_pl.txt",
            "2_pl.txt",
            "3_pl.txt",
            "4_pl.txt",
            "5_pl.txt",
            "6_pl.txt",
            "7_pl.txt",
            "8_pl.txt",
            "9_pl.txt",
            "10_pl.txt",
        ],
        "slowacki": [
            "1_sk.txt",
            "2_sk.txt",
            "3_sk.txt",
            "4_sk.txt",
            "5_sk.txt",
            "6_sk.txt",
            "7_sk.txt",
            "8_sk.txt",
            "9_sk.txt",
            "10_sk.txt",
        ],
        "czeski": [
            "1_cz.txt",
            "2_cz.txt",
            "3_cz.txt",
            "4_cz.txt",
            "5_cz.txt",
            "6_cz.txt",
            "7_cz.txt",
            "8_cz.txt",
            "9_cz.txt",
            "10_cz.txt",
        ]
    }

    dane = zaladuj_dane(training_files)
    if not dane:
        print("Brak danych treningowych :<<")
        return

    perceptrony = trening_perceptronow(dane, a=0.1, epoki=1000)
    print("\nTrening zakończony.")

    while True:
        print("\nPodaj tekst do klasyfikacji (ENTER -> WYJŚCIE):")
        wejscie = input()

        if wejscie.lower() == '':
            break

        jezyk, wyniki = klasyfikuj_tekst(wejscie, perceptrony)

        print(f"Język: {jezyk}")

        for lang, score in wyniki.items():
            print(f"  {lang}: {score:.4f}")


if __name__ == "__main__":
    main()