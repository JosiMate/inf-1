# -*- coding: utf-8 -*-
"""
Znajdowanie drogi wyjścia z labiryntu — szkielet do ćwiczeń.
Klasa 3, informatyka w zakresie rozszerzonym, PCEiKZ Szczucin.

Uzupełnij funkcje oznaczone słowem TODO, a potem uruchom ten plik.
Testy na dole sprawdzą twoje rozwiązanie i wypiszą, co przechodzi,
a co nie. Nie zmieniaj treści testów — zmieniaj funkcje.

Umowa co do danych: labirynt jest listą napisów jednakowej długości,
otoczoną ramką ze ścian. Znaki:
    '#' ściana, '.' wolne pole, 'S' start, 'E' wyjście
Pole opisuje krotka (w, k) — numer wiersza i numer kolumny, od zera.
Droga to lista pól od startu do wyjścia włącznie.
"""
import sys
from collections import deque

# Kolejność sprawdzania sąsiadów: góra, prawo, dół, lewo.
# Ta sama dla obu algorytmów — inaczej porównanie nie byłoby uczciwe.
KIERUNKI = ((-1, 0), (0, 1), (1, 0), (0, -1))


def znajdz(lab, znak):
    """Zwraca współrzędne pierwszego pola z danym znakiem albo None."""
    for w, wiersz in enumerate(lab):
        k = wiersz.find(znak)
        if k != -1:
            return (w, k)
    return None


# ─────────────────────────────────────────────────────── ZADANIE 1
def sasiedzi(lab, pole):
    """Zwraca listę pól sąsiadujących z danym, po których można chodzić.

    Kolejność musi być zgodna z KIERUNKI, a ściany ('#') odpadają.
    Dzięki ramce ze ścian nie trzeba sprawdzać wyjścia poza tablicę —
    ale jeśli wolisz sprawdzać, nic złego się nie stanie.
    """
    w, k = pole
    wynik = []
    for dw, dk in KIERUNKI:
        pass  # TODO: dopisz sąsiada do listy, jeżeli nie jest ścianą
    return wynik


# ─────────────────────────────────────────────────────── ZADANIE 2
def szukaj_rekurencyjnie(lab, start=None, wyjscie=None):
    """Szuka drogi metodą przeszukiwania z nawrotami (rekurencyjnie).

    Zwraca listę pól od startu do wyjścia albo None, gdy wyjścia nie ma.

    Schemat funkcji pomocniczej idz(pole):
      • jeżeli pole odwiedzone → False
      • oznacz jako odwiedzone, dopisz do drogi
      • jeżeli to wyjście → True
      • dla każdego sąsiada: jeżeli idz(sąsiad) → True
      • NAWRÓT: zdejmij pole z drogi, zwróć False
    """
    start = start or znajdz(lab, "S")
    wyjscie = wyjscie or znajdz(lab, "E")
    odwiedzone = set()
    droga = []

    def idz(pole):
        return False  # TODO: napisz treść funkcji według schematu wyżej

    return droga if idz(start) else None


def licz_nawroty(lab, start=None, wyjscie=None):
    """Jak wyżej, ale zwraca parę (droga, liczba wykonanych nawrotów).

    Nawrót to każde zdjęcie pola z drogi. Wystarczy dopisać licznik
    do rozwiązania z poprzedniej funkcji.
    """
    return (None, 0)  # TODO


# ─────────────────────────────────────────────────────── ZADANIE 3
def odtworz(skad, start, wyjscie):
    """Odtwarza drogę, idąc wstecz po mapie „skąd”, i odwraca wynik.

    skad[pole] to pole, z którego weszliśmy na `pole`. Start nie ma wpisu.
    """
    droga = [wyjscie]
    # TODO: dopóki ostatnie pole nie jest startem, dopisuj skad[...]
    return droga


def najkrotsza_droga(lab, start=None, wyjscie=None):
    """Szuka NAJKRÓTSZEJ drogi metodą przeszukiwania wszerz (kolejka).

    Zwraca listę pól od startu do wyjścia albo None, gdy wyjścia nie ma.

    Schemat:
      • start do kolejki, oznacz jako odwiedzony
      • dopóki kolejka niepusta: zdejmij pole Z POCZĄTKU (popleft)
      • jeżeli to wyjście → zwróć odtworz(skad, start, wyjscie)
      • każdy nieodwiedzony sąsiad: oznacz, zapisz skad, dołóż NA KONIEC
    """
    start = start or znajdz(lab, "S")
    wyjscie = wyjscie or znajdz(lab, "E")
    kolejka = deque([start])
    odwiedzone = {start}
    skad = {}

    while kolejka:
        pole = kolejka.popleft()
        # TODO: jeżeli pole jest wyjściem → zwróć odtworz(skad, start, wyjscie)
        # TODO: dla każdego nieodwiedzonego sąsiada: oznacz, zapisz skad,
        #       dołóż na koniec kolejki
    return None


# ─────────────────────────────────────── ZADANIE 4 (na ocenę wyższą)
def szukaj_iteracyjnie(lab, start=None, wyjscie=None):
    """To samo co szukaj_rekurencyjnie, ale bez rekurencji.

    Na stosie trzymaj pary [pole, indeks kolejnego kierunku do sprawdzenia].
    Gdy indeks dojdzie do czterech, wszystkie kierunki zawiodły — zdejmij
    parę ze stosu (to jest nawrót).
    """
    return None  # TODO


# ══════════════════════════════════════════════════ LABIRYNTY
MALY = [
    "#######",
    "#S.#..#",
    "#.#..E#",
    "#...#.#",
    "#######",
]

PLASZCZ = [
    "#############",
    "#S..........#",
    "#.#####.###.#",
    "#.........#.#",
    "###.#####.#.#",
    "#...#.....#.#",
    "#.###.#.#.#.#",
    "#......E....#",
    "#############",
]

# Labirynt doskonały: bez cykli, więc z S do E prowadzi dokładnie jedna droga.
JEDNA_DROGA = [
    "###########",
    "#S#...#...#",
    "#.#.#.###.#",
    "#...#...#.#",
    "#######.#.#",
    "#........E#",
    "###########",
]

BEZ_WYJSCIA = [
    "#######",
    "#S....#",
    "#.###.#",
    "#...#.#",
    "###.###",
    "#..#.E#",      # wyjście odcięte ścianą
    "#######",
]


def waz(dlugosc=1400):
    """Długi kręty korytarz — po to, żeby przewrócić rekurencję.

    Buduje labirynt o `dlugosc` wolnych polach ułożonych w wężyk.
    Droga ma tu tyle samo pól co cały labirynt, więc rekurencja schodzi
    na taką właśnie głębokość.
    """
    kolumny = 21
    wiersze = max(3, (dlugosc // (kolumny - 2)) * 2 + 1)
    plan = []
    for w in range(wiersze):
        if w % 2 == 0:
            plan.append(list("#" + "." * (kolumny - 2) + "#"))
        else:
            # co drugi wiersz zostawia jedno przejście, raz przy lewej,
            # raz przy prawej krawędzi — stąd wężyk
            wiersz = list("#" * kolumny)
            wiersz[1 if (w // 2) % 2 else kolumny - 2] = "."
            plan.append(wiersz)
    plan[0][1] = "S"
    plan[-1][kolumny - 2 if (len(plan) // 2) % 2 == 0 else 1] = "E"
    return ["#" * kolumny] + ["".join(w) for w in plan] + ["#" * kolumny]


def rysuj(lab, droga=None):
    """Wypisuje labirynt, zaznaczając drogę gwiazdkami."""
    na_drodze = set(droga or ())
    for w, wiersz in enumerate(lab):
        print("  " + "".join(
            "*" if (w, k) in na_drodze and z not in "SE" else z
            for k, z in enumerate(wiersz)))


def porownaj():
    """Tabelka jak w sekcji 4 materiału — dla wszystkich labiryntów."""
    print(f"\n{'labirynt':12s} {'nawroty':>10s} {'wszerz':>10s}")
    for nazwa, lab in (("MALY", MALY), ("PLASZCZ", PLASZCZ),
                       ("JEDNA_DROGA", JEDNA_DROGA), ("BEZ_WYJSCIA", BEZ_WYJSCIA)):
        d = szukaj_rekurencyjnie(lab)
        b = najkrotsza_droga(lab)
        print(f"{nazwa:12s} {len(d) if d else '—':>10} {len(b) if b else '—':>10}")


# ══════════════════════════════════════════════════════ TESTY
def _spojna(lab, droga, start, wyjscie):
    """Czy droga zaczyna się w S, kończy w E, omija ściany i nie skacze?"""
    if not droga or droga[0] != start or droga[-1] != wyjscie:
        return False
    for (w, k) in droga:
        if lab[w][k] == "#":
            return False
    for (w1, k1), (w2, k2) in zip(droga, droga[1:]):
        if abs(w1 - w2) + abs(k1 - k2) != 1:
            return False
    return True


def sprawdz():
    zaliczone, wszystkie = 0, 10

    print("Zadanie 1 — sąsiedzi")
    try:
        wynik = sasiedzi(MALY, (1, 1))
        ok = wynik == [(1, 2), (2, 1)]          # góra i lewo to ściany
    except Exception as blad:
        wynik, ok = f"błąd: {blad}", False
    print(f"  {'OK  ' if ok else 'ŹLE '} sasiedzi(MALY, (1,1)) = {wynik}   (oczekiwane [(1, 2), (2, 1)])")
    zaliczone += ok

    print("\nZadanie 2 — przeszukiwanie z nawrotami")
    for nazwa, lab, dlugosc in (("MALY", MALY, 10), ("PLASZCZ", PLASZCZ, 45)):
        try:
            droga = szukaj_rekurencyjnie(lab)
            ok = _spojna(lab, droga, znajdz(lab, "S"), znajdz(lab, "E")) and len(droga) == dlugosc
        except Exception as blad:
            droga, ok = f"błąd: {blad}", False
        ile = len(droga) if isinstance(droga, list) else droga
        print(f"  {'OK  ' if ok else 'ŹLE '} {nazwa:12s} droga ma {ile} pól   (oczekiwane {dlugosc})")
        zaliczone += ok

    try:
        ok = szukaj_rekurencyjnie(BEZ_WYJSCIA) is None
    except Exception as blad:
        ok = False
        print(f"       błąd: {blad}")
    print(f"  {'OK  ' if ok else 'ŹLE '} BEZ_WYJSCIA  zwraca None")
    zaliczone += ok

    try:
        _, nawroty = licz_nawroty(MALY)
        ok = nawroty == 1
    except Exception as blad:
        nawroty, ok = f"błąd: {blad}", False
    print(f"  {'OK  ' if ok else 'ŹLE '} MALY         nawrotów: {nawroty}   (oczekiwany 1)")
    zaliczone += ok

    print("\nZadanie 3 — najkrótsza droga (kolejka)")
    for nazwa, lab, dlugosc in (("MALY", MALY, 8), ("PLASZCZ", PLASZCZ, 17),
                                ("JEDNA_DROGA", JEDNA_DROGA, 17)):
        try:
            droga = najkrotsza_droga(lab)
            ok = _spojna(lab, droga, znajdz(lab, "S"), znajdz(lab, "E")) and len(droga) == dlugosc
        except Exception as blad:
            droga, ok = f"błąd: {blad}", False
        ile = len(droga) if isinstance(droga, list) else droga
        print(f"  {'OK  ' if ok else 'ŹLE '} {nazwa:12s} droga ma {ile} pól   (oczekiwane {dlugosc})")
        zaliczone += ok

    try:
        ok = najkrotsza_droga(BEZ_WYJSCIA) is None
    except Exception as blad:
        ok = False
        print(f"       błąd: {blad}")
    print(f"  {'OK  ' if ok else 'ŹLE '} BEZ_WYJSCIA  zwraca None")
    zaliczone += ok

    print("\nZadanie 4 — wersja iteracyjna (na ocenę wyższą)")
    lab = waz()
    wolnych = sum(w.count(".") + w.count("S") + w.count("E") for w in lab)
    print(f"  labirynt WAZ ma {wolnych} wolnych pól, a limit zagnieżdżeń "
          f"wynosi {sys.getrecursionlimit()}")
    try:
        szukaj_rekurencyjnie(lab)
        print("     rekurencja przeszła (podniesiony limit? krótszy wąż?)")
    except RecursionError:
        print("     rekurencja: RecursionError — dokładnie tak, jak zapowiadał materiał")
    except Exception as blad:
        print(f"     rekurencja: {blad}")
    try:
        droga = szukaj_iteracyjnie(lab)
        ok = _spojna(lab, droga, znajdz(lab, "S"), znajdz(lab, "E"))
        print(f"  {'OK  ' if ok else 'ŹLE '} wersja iteracyjna: droga {len(droga) if droga else '—'} pól")
    except Exception as blad:
        ok = False
        print(f"  ŹLE  wersja iteracyjna: błąd: {blad}")
    zaliczone += ok

    print(f"\nZaliczone: {zaliczone} z {wszystkie}")
    if zaliczone == wszystkie:
        print("Wszystko działa. Uruchom porownaj() i zajrzyj do zadań na ocenę celującą.")


if __name__ == "__main__":
    # Limitu rekurencji celowo NIE podnosimy — labirynt WAZ ma go przekroczyć.
    sprawdz()
