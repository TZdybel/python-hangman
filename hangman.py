import random
import sys

def writeToArray(words):
    a = 0  # zmienna pomocnicza, potrzebna do zakonczenie przeszukania pliku
    filepath = "slowa.txt"  # wprowadzam nazwe/sciezke do pliku
    numOfWords = 0

    try:
        file = open(filepath)
        file.seek(0,
                  2)  # przesuwam wskaznik na koniec pliku: 0 - ilość bajtów do przesuniecia, 2 - oznacza od konca pliku (0 to poczatek, 1 to aktualna pozycja)
        a = file.tell()  # zapisuje indeks wskaznika w zmiennej a
        file.seek(0, 0)  # przesuwam z powrotem na poczatek
    except FileNotFoundError:
        print("Entered file does not exists")
    except IOError:
        print("Something went wrong with a file")

    try:
        while file.tell() < a:  # przegladamy plik dopoki nie dojdzie on do konca pliku
            words.append(file.readline().strip())  # do tablicy dodajemy po kolei slowa z pliku
            numOfWords += 1
    except IOError:
        print("Something went wrong with a file")
    finally:
        file.close()

    return numOfWords

def drawMysteryWord(words, numOfWords):
    random.seed()  # odpowiednik srand, uzywa aktualnego czasu do wygenerowania danych pseudolosowych
    a = random.randint(0, numOfWords - 1)  # losujemy slowo z listy

    mysteryWord = words[a]  # zapisujemy nasze wylosowane slowo pod zmienna

    return mysteryWord

def playHangman(mysteryWord):

    length = len(mysteryWord)

    print("")  # przejscie do nowej linii

    notGuessed = length  # zmienna przetrzymujaca dane o tym, ile jeszcze liter pozostalo do zgadniecia
    lives = 3  # liczba bledow, max 3
    hit = False  # flaga przetrzymujaca informacje, czy przy danej probie zgadlismy cos, czy nie

    guessed = []  # tablica, w ktorej przetrzymujemy informacje, ktore litery zostaly juz odgadniete, jesli jest False - nieodgadnieta, True - odgadnieta

    i = 0  # zmienna pomocnicza
    while i < length:
        guessed.append(False)  # wypelniamy tablice False'ami
        sys.stdout.write("_ ")  # wypisywanie na ekran bez przejscia do nowej linii
        i += 1

    sys.stdout.write(" If you want to enter whole word, just do it! :) ")
    while notGuessed > 0:
        pom = input()  # pobieramy litere
        isAlphabetical = False
        while not isAlphabetical:  # sprawdzamy czy sa tylko litery alfabetu
            if not pom.isalpha():
                print("There are some inappropriate signs, you can enter only letters")
                pom = input()
            else:
                isAlphabetical = True
        if pom == mysteryWord:  # sprawdzamy, czy nie podano dobrego slowa
            for c in mysteryWord:
                sys.stdout.write(c + " ")
            print(" Congrats! :)")
            break
        hit = False
        tmp = 0
        while tmp < length:
            if pom == mysteryWord[tmp] and not guessed[tmp]:  # jesli trafiona
                sys.stdout.write(mysteryWord[tmp] + " ")  # wypisujemy
                hit = True  # flaga na True
                notGuessed -= 1  # zmniejszamy liczbe liter do zgadniecia o 1
                guessed[tmp] = True  # ustawiamy flage, ze ta pozycja zostala odgadnieta
            elif guessed[tmp]:
                sys.stdout.write(mysteryWord[tmp] + " ")  # jesli wczesniej odgadnieta, wypisujemy
            else:
                sys.stdout.write("_ ")
            tmp += 1
        if not hit:  # jesli nie trafiona, odejmujemy jedno zycie
            lives -= 1
            print(" Lives left: " + str(lives))
        if lives == 0:  # przegrana
            print("\nYOU'VE LOST!")
            print("ANSWER: " + mysteryWord)
            break

    if notGuessed == 0:  # wygrana
        print(" Congrats! :)")

def main():
    words = []  # tablica slow, do niej wczytywane sa kolejne slowa z pliku
    numOfWords = writeToArray(words)  # zmienna zliczajaca ile jest slow w pliku
    playHangman(drawMysteryWord(words, numOfWords))


if __name__=="__main__":
    main()