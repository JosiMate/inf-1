# -*- coding: utf-8 -*-
"""
Odwrotna notacja polska — szkielet do ćwiczeń.
Klasa 3, informatyka w zakresie rozszerzonym, PCEiKZ Szczucin.

Uzupełnij trzy funkcje oznaczone słowem TODO, a potem uruchom ten plik.
Testy na dole sprawdzą twoje rozwiązanie i wypiszą, co przechodzi,
a co nie. Nie zmieniaj treści testów — zmieniaj funkcje.

Umowa co do danych wejściowych: wyrażenie jest napisem, w którym liczby,
operatory i nawiasy są rozdzielone pojedynczymi spacjami, na przykład
    "( 3 + 4 ) * 2"
Dzięki temu nie musisz pisać własnego analizatora leksykalnego i możesz
skupić się na algorytmie.
"""

PRIORYTET = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
PRAWOSTRONNE = {"^"}          # 2 ^ 3 ^ 2 liczymy jako 2 ^ (3 ^ 2)


def podziel(wyrazenie):
    """Dzieli napis na listę symboli (tokenów)."""
    return wyrazenie.split()


# ─────────────────────────────────────────────────────── ZADANIE 1
def oblicz_onp(wyrazenie):
    """Oblicza wartość wyrażenia zapisanego w ONP, używając stosu.

    Algorytm:
      • liczba          → odłóż na stos
      • operator        → zdejmij DWA elementy, wykonaj działanie,
                          wynik odłóż z powrotem na stos
      • na końcu na stosie zostaje jedna liczba — to wynik

    Uwaga na kolejność przy odejmowaniu i dzieleniu: pierwszy zdjęty
    element jest PRAWYM argumentem działania.
    """
    stos = []
    for token in podziel(wyrazenie):
        pass  # TODO: napisz treść pętli
    return None  # TODO: zwróć wynik ze stosu


# ─────────────────────────────────────────────────────── ZADANIE 2
def na_onp(wyrazenie):
    """Zamienia zapis tradycyjny (infiksowy) na ONP.

    Algorytm stacji rozrządowej (Dijkstra):
      • liczba          → od razu do wyniku
      • operator        → dopóki na szczycie stosu stoi operator
                          o wyższym priorytecie (albo równym, gdy
                          bieżący jest lewostronny) — przenieś go
                          ze stosu do wyniku; potem odłóż bieżący
      • nawias otwierający  → na stos
      • nawias zamykający   → przenoś ze stosu do wyniku, aż trafisz
                              na nawias otwierający; jego samego usuń
      • na końcu przenieś ze stosu do wyniku wszystko, co zostało
    """
    wynik, stos = [], []
    for token in podziel(wyrazenie):
        pass  # TODO: napisz treść pętli
    return " ".join(wynik)


# ─────────────────────────────────────────────────────── ZADANIE 3
def slad_obliczen(wyrazenie):
    """Zwraca listę stanów stosu po każdym kroku obliczania ONP.

    Dla "3 4 +" ma zwrócić [[3.0], [3.0, 4.0], [7.0]].
    Przyda się w karcie pracy — i przy szukaniu własnych błędów.
    """
    return []  # TODO


# ═══════════════════════════════════════════════════════ TESTY
TESTY_ONP = [
    ("3 4 +", 7),
    ("5 1 2 + 4 * + 3 -", 14),
    ("2 3 ^", 8),
    ("6 2 /", 3),
    ("4 2 5 * + 1 3 2 * + /", 2),
]

TESTY_ZAMIANY = [
    ("3 + 4", "3 4 +"),
    ("3 + 4 * 2", "3 4 2 * +"),
    ("( 3 + 4 ) * 2", "3 4 + 2 *"),
    ("5 + ( 1 + 2 ) * 4 - 3", "5 1 2 + 4 * + 3 -"),
    ("2 ^ 3 ^ 2", "2 3 2 ^ ^"),      # potęgowanie łączy się w prawo
    ("10 - 4 - 3", "10 4 - 3 -"),    # odejmowanie łączy się w lewo
]


def sprawdz():
    zaliczone = 0
    wszystkie = len(TESTY_ONP) + len(TESTY_ZAMIANY) + 1

    print("Zadanie 1 — obliczanie wartości wyrażenia w ONP")
    for wejscie, oczekiwane in TESTY_ONP:
        try:
            wynik = oblicz_onp(wejscie)
            ok = wynik is not None and abs(wynik - oczekiwane) < 1e-9
        except Exception as blad:
            wynik, ok = f"błąd: {blad}", False
        print(f"  {'OK  ' if ok else 'ŹLE '} {wejscie:24s} = {wynik}   (oczekiwane {oczekiwane})")
        zaliczone += ok

    print("\nZadanie 2 — zamiana zapisu tradycyjnego na ONP")
    for wejscie, oczekiwane in TESTY_ZAMIANY:
        try:
            wynik = na_onp(wejscie)
            ok = wynik == oczekiwane
        except Exception as blad:
            wynik, ok = f"błąd: {blad}", False
        print(f"  {'OK  ' if ok else 'ŹLE '} {wejscie:24s} → {wynik}   (oczekiwane {oczekiwane})")
        zaliczone += ok

    print("\nZadanie 3 — ślad obliczeń")
    try:
        slad = slad_obliczen("3 4 +")
        ok = slad == [[3.0], [3.0, 4.0], [7.0]]
    except Exception as blad:
        slad, ok = f"błąd: {blad}", False
    print(f"  {'OK  ' if ok else 'ŹLE '} ślad dla 3 4 + = {slad}")
    zaliczone += ok

    print(f"\nZaliczone: {zaliczone} z {wszystkie}")
    if zaliczone == wszystkie:
        print("Wszystko działa. Zajrzyj teraz do zadań na ocenę celującą.")


if __name__ == "__main__":
    sprawdz()
