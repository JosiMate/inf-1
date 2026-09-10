# Znajdowanie drogi wyjścia z labiryntu

!!! abstract "O tym temacie"

    **4 godziny lekcyjne** · Dział II. Rozwiązywanie problemów z wykorzystaniem
    dynamicznych struktur danych · podstawa programowa **I.1, I.3, RI.2, RI.3,
    RI.4, RI.5, RI.10, II.1, RII.1, RII.2**

    Ten sam labirynt, ten sam kod poza jedną linijką — a wynik zupełnie inny.
    Wymienisz **stos** na **kolejkę** i z „jakiejś drogi" robi się droga
    **najkrótsza**. To najbardziej pouczający przykład na to, że struktura
    danych bywa ważniejsza od algorytmu.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. zapisać labirynt jako siatkę i wyznaczyć sąsiadów danego pola
    2. wyjaśnić, na czym polega przeszukiwanie z nawrotami (*backtracking*)
    3. zaimplementować rekurencyjny algorytm znajdujący wyjście z labiryntu
    4. wymienić operacje na kolejce i wskazać, czym różni się ona od stosu
    5. zaimplementować iteracyjny algorytm z kolejką i odtworzyć znalezioną drogę
    6. uzasadnić, dlaczego kolejka daje drogę najkrótszą, a stos byle jaką
    7. porównać obie wersje pod względem złożoności czasowej i zużycia pamięci

## 1. Labirynt to graf, tylko narysowany

Zadanie brzmi prosto: dany jest labirynt, wskaż drogę od wejścia do wyjścia.
Żeby komputer mógł je rozwiązać, trzeba najpierw powiedzieć, **czym jest
labirynt** z punktu widzenia programu.

Najwygodniej zapisać go jako **prostokątną siatkę znaków**:

```text
#######
#S.#..#
#.#..E#
#...#.#
#######
```

- `#` — ściana, przez którą nie da się przejść
- `.` — wolne pole
- `S` — start (*start*)
- `E` — wyjście (*exit*)

Pole ma współrzędne `(w, k)` — numer wiersza i numer kolumny, liczone od zera,
jak indeksy w liście list. Z pola `(w, k)` można przejść na **cztery** sąsiednie:

| Kierunek | Współrzędne sąsiada |
| --- | --- |
| góra | `(w - 1, k)` |
| prawo | `(w, k + 1)` |
| dół | `(w + 1, k)` |
| lewo | `(w, k - 1)` |

To już jest **graf**: pola to wierzchołki, sąsiedztwo to krawędzie. Różnica
wobec grafu z rysunku jest wyłącznie taka, że listy sąsiadów nie musimy nigdzie
przechowywać — wyliczamy ją z współrzędnych, kiedy jest potrzebna.

!!! tip "Ramka ze ścian to strażnik"

    Wszystkie nasze labirynty mają dookoła ramkę z `#`. Dzięki temu nie trzeba
    sprawdzać, czy indeks nie wyszedł poza tablicę — wystarczy sprawdzić, czy
    pole nie jest ścianą. Taki celowo wstawiony element, który upraszcza warunki
    brzegowe, nazywa się **strażnikiem** (*sentinel*) i spotkasz go jeszcze
    nieraz: w listach, w wyszukiwaniu, w sortowaniu.

Problem jest praktyczny, nie tylko szkolny. Tym samym algorytmem robot omija
przeszkody w pomieszczeniu, nawigacja szuka trasy w siatce ulic, a gra
sprawdza, czy przeciwnik ma jak dojść do gracza.

## 2. Przeszukiwanie z nawrotami

Wyobraź sobie, że idziesz labiryntem z kredą w ręku. Zasady są trzy:

1. Wchodząc na pole, **zamaluj je** — żeby nie chodzić w kółko.
2. Idź na dowolne sąsiednie pole, które nie jest ścianą i nie jest zamalowane.
3. Jeśli takiego nie ma — **wróć** na pole, z którego przyszedłeś, i próbuj dalej stamtąd.

Punkt 3 to właśnie **nawrót** (*backtracking*), a cała metoda nazywa się
**przeszukiwaniem z nawrotami**. Ślepy zaułek nie kończy poszukiwań — cofa je
o jeden krok.

Zwróć uwagę, gdzie siedzi droga: w **kolejności odwiedzania pól**, do których
jeszcze nie było nawrotu. Jeśli zapisujesz tę kolejność na stosie, to stos
w każdej chwili zawiera **całą trasę od startu do miejsca, w którym stoisz** —
i w momencie dojścia do wyjścia masz gotową odpowiedź, bez odtwarzania czegokolwiek.

### Wersja rekurencyjna

Rekurencja robi to samo, tylko stosem jest wtedy **stos wywołań funkcji**
utrzymywany przez Pythona:

```python
def szukaj(lab, w, k, odwiedzone, droga):
    """Zwraca True, jeśli z pola (w, k) da się dojść do wyjścia.
    Znalezioną drogę zostawia w liście droga."""
    if lab[w][k] == "#" or (w, k) in odwiedzone:
        return False                     # ściana albo już tu byliśmy

    odwiedzone.add((w, k))
    droga.append((w, k))                 # wchodzę na pole

    if lab[w][k] == "E":
        return True                      # jestem u celu — droga jest w liście

    for dw, dk in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if szukaj(lab, w + dw, k + dk, odwiedzone, droga):
            return True                  # któryś sąsiad się udał

    droga.pop()                          # NAWRÓT: to pole do niczego nie prowadzi
    return False
```

Cała istota nawrotu mieści się w przedostatniej linijce. Wywołanie kończy się
niepowodzeniem dopiero wtedy, gdy zawiodły **wszystkie cztery** kierunki —
i wtedy pole znika z drogi.

!!! danger "Rekurencja ma dno"

    Python domyślnie przerywa program po około **1000** zagnieżdżonych wywołań
    (`RecursionError`). Jedno wywołanie to jedno pole drogi, więc labirynt
    50 × 50 — czyli 2500 pól — potrafi to dno przebić.

    `sys.setrecursionlimit(10000)` odsuwa problem, ale go nie usuwa: prawdziwy
    stos wywołań jest ograniczony pamięcią procesu, a jego przepełnienie kończy
    się już nie wyjątkiem, tylko zamknięciem programu. Dla dużych danych
    właściwym rozwiązaniem jest wersja iteracyjna z własnym stosem — ta sama
    logika, tylko stos trzymamy w liście, a nie w wywołaniach.

### Ślad krok po kroku

Prześledźmy labirynt z sekcji 1, sprawdzając sąsiadów w kolejności
**góra → prawo → dół → lewo**. Start `(1,1)`, wyjście `(2,5)`.

| Krok | Stoję na | Co robię | Stos (= droga) po kroku |
| :---: | :---: | --- | --- |
| 1 | `(1,1)` | góra to ściana, w prawo wolne — idę na `(1,2)` | `(1,1) (1,2)` |
| 2 | `(1,2)` | dookoła same ściany — **nawrót** | `(1,1)` |
| 3 | `(1,1)` | zostaje dół — idę na `(2,1)` | `(1,1) (2,1)` |
| 4 | `(2,1)` | idę na `(3,1)` | `(1,1) (2,1) (3,1)` |
| 5 | `(3,1)` | idę na `(3,2)` | `(1,1) (2,1) (3,1) (3,2)` |
| 6 | `(3,2)` | idę na `(3,3)` | `(1,1) (2,1) (3,1) (3,2) (3,3)` |
| … | | dalej bez nawrotów: `(2,3) (2,4) (1,4) (1,5)` | |
| 12 | `(2,5)` | **wyjście** — na stosie leży gotowa droga | 10 pól |

Pole `(1,2)` było ślepym zaułkiem i zostało z drogi zdjęte. Nie zniknęło jednak
ze zbioru **odwiedzonych** — dlatego algorytm nigdy tam nie wróci.

!!! warning "Odwiedzone i droga to dwa różne zbiory"

    Częsty błąd: usunięcie pola z `odwiedzone` przy nawrocie, „bo przecież
    z niego zrezygnowaliśmy". Wtedy algorytm potrafi wejść w ten sam ślepy
    zaułek wielokrotnie, a w labiryncie z cyklem — zapętlić się na dobre.

    **Droga** kurczy się przy nawrocie. **Odwiedzone** rosną i nigdy nie maleją.

## 3. Kolejka i najkrótsza droga

Droga znaleziona przez nawroty jest poprawna, ale **byle jaka** — to po prostu
pierwsza, na którą algorytm trafił. Jeśli pytanie brzmi „ile najmniej ruchów
dzieli mnie od wyjścia", potrzebna jest inna struktura danych.

### Kolejka

**Kolejka** to dynamiczna struktura działająca według zasady **FIFO**
(*first in, first out*) — pierwszy włożony wychodzi pierwszy. Jak kolejka
w sklepie, w odróżnieniu od stosu talerzy.

| Operacja | Co robi | W Pythonie (`deque`) |
| --- | --- | --- |
| `enqueue` | dokłada element **na koniec** | `kolejka.append(x)` |
| `dequeue` | zdejmuje i zwraca element **z początku** | `kolejka.popleft()` |
| `front` | podgląda początek, nie zdejmując | `kolejka[0]` |
| `isEmpty` | sprawdza, czy kolejka jest pusta | `not kolejka` |

!!! warning "Zwykła lista kolejką nie jest"

    `lista.pop(0)` zdejmuje z początku — ale przy okazji **przesuwa wszystkie
    pozostałe elementy o jedno miejsce**, więc kosztuje czas proporcjonalny do
    długości listy. Kolejka zbudowana na liście działa więc w czasie O(n²)
    zamiast O(n) i przy większym labiryncie robi się boleśnie wolna.

    `collections.deque` ma dostęp z obu końców w czasie stałym i to jej należy
    tu użyć. (Na stos lista wystarcza w zupełności — `append` i `pop` bez
    argumentu działają na końcu, czyli tam, gdzie trzeba.)

### Przeszukiwanie wszerz

Algorytm z kolejką nazywa się **przeszukiwaniem wszerz** (*breadth-first
search*, **BFS**) i różni się od poprzedniego jednym: zamiast schodzić
w głąb jednej trasy, obchodzi labirynt **falą**.

1. Włóż start do kolejki i oznacz jako odwiedzony.
2. Dopóki kolejka nie jest pusta: zdejmij pole z **początku**.
3. Jeśli to wyjście — koniec.
4. W przeciwnym razie każdego nieodwiedzonego sąsiada oznacz jako odwiedzonego,
   **zapamiętaj, skąd do niego przyszedłeś**, i dołóż go na **koniec** kolejki.

```python
from collections import deque

def najkrotsza(lab, start, wyjscie):
    kolejka = deque([start])
    odwiedzone = {start}
    skad = {}                            # pole → pole, z którego tu weszliśmy

    while kolejka:
        w, k = kolejka.popleft()
        if (w, k) == wyjscie:
            return odtworz(skad, start, wyjscie)

        for dw, dk in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            sasiad = (w + dw, k + dk)
            if lab[sasiad[0]][sasiad[1]] != "#" and sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                skad[sasiad] = (w, k)
                kolejka.append(sasiad)
    return None                          # kolejka pusta — wyjścia nie ma
```

### Odtwarzanie drogi

Tu jest różnica, którą łatwo przeoczyć. Przy nawrotach stos **był** drogą.
Kolejka drogą nie jest — leżą w niej pola z różnych tras naraz. Dlatego przy
każdym polu zapisujemy, **skąd** do niego weszliśmy, a na końcu idziemy tym
zapisem wstecz, od wyjścia do startu, i odwracamy wynik:

```python
def odtworz(skad, start, wyjscie):
    droga = [wyjscie]
    while droga[-1] != start:
        droga.append(skad[droga[-1]])
    droga.reverse()
    return droga
```

### Dlaczego to jest najkrótsza droga

Popatrz na mapę odległości od startu dla naszego labiryntu — liczba w polu to
najmniejsza liczba ruchów potrzebna, żeby się na nie dostać:

```text
##  ##  ##  ##  ##  ##  ##
##   0   1  ##   7   8  ##
##   1  ##   5   6   7  ##
##   2   3   4  ##   8  ##
##  ##  ##  ##  ##  ##  ##
```

Kolejka układa pola **w kolejności rosnącej odległości**: najpierw wszystkie
w jednym ruchu od startu, potem wszystkie w dwóch, i tak dalej. Nowe pole
trafia na koniec kolejki, więc zostanie obsłużone dopiero po wszystkich
wcześniejszymi — a to dokładnie te bliższe.

Skoro więc pola wychodzą z kolejki po kolei według odległości, to w chwili,
gdy z kolejki wychodzi **wyjście**, żadna krótsza droga do niego istnieć nie
może — bo zostałaby znaleziona wcześniej. Wyjście `(2,5)` ma odległość 7,
czyli droga liczy 8 pól. Nawroty znalazły 10.

!!! info "To działa, bo każdy ruch kosztuje tyle samo"

    BFS daje najkrótszą drogę pod warunkiem, że **wszystkie krawędzie mają
    równą wagę** — tu każdy ruch to jedno pole. Gdy przejścia różnią się kosztem
    (błoto wolniejsze niż droga, ulice różnej długości), sama kolejka nie
    wystarcza i potrzebny jest **algorytm Dijkstry**. To temat następnej lekcji
    z tego działu.

## 4. Zobacz różnicę

Ten sam labirynt, ta sama kolejność sprawdzania sąsiadów. Zmienia się wyłącznie
struktura danych. Przełącz algorytm i przeklikaj oba do końca — albo puść
„Do końca" i popatrz, jak się rozchodzą.

<div class="labirynt" markdown="0">
<script type="application/json">
{
  "tryb": "dfs",
  "siatka": [
    "#############",
    "#S..........#",
    "#.#####.###.#",
    "#.........#.#",
    "###.#####.#.#",
    "#...#.....#.#",
    "#.###.#.#.#.#",
    "#......E....#",
    "#############"
  ]
}
</script>
</div>

Dla tego labiryntu wyniki są takie:

| | Nawroty (stos) | Wszerz (kolejka) |
| --- | :---: | :---: |
| długość znalezionej drogi | **45 pól** | **17 pól** |
| odwiedzonych pól | 47 | 52 |
| co gwarantuje | *jakąś* drogę | drogę **najkrótszą** |

Stos poszedł pierwszym korytarzem w prawo i przeszedł prawie cały labirynt,
zanim natknął się na wyjście — drogę ma prawie trzykrotnie dłuższą. Kolejka
obeszła o pięć pól więcej, ale odpowiedź dała optymalną.

!!! quote "Kiedy które"

    - **Nawroty** — gdy wystarczy *czy w ogóle się da* i *którędy jakkolwiek*,
      a labirynt jest duży: pamięć zajmuje tylko bieżąca droga.
    - **Wszerz** — gdy pytanie brzmi *najkrócej* albo *ile ruchów*: pamięć
      zajmuje cała fala, ale odpowiedź jest optymalna.

## 5. Złożoność

Oba algorytmy odwiedzają każde pole **najwyżej raz** i przy każdym sprawdzają
czterech sąsiadów. Dla labiryntu o `n` polach daje to liczbę operacji
proporcjonalną do `n` — **złożoność liniowa, O(n)**. Dla siatki `w` × `k`
oznacza to `O(w · k)`.

Różnica siedzi w **pamięci**:

| | Pamięć w najgorszym przypadku | Co ją zajmuje |
| --- | --- | --- |
| nawroty | O(n) | stos = bieżąca droga; w wężowym korytarzu obejmuje wszystkie pola |
| wszerz | O(n) | kolejka + mapa `skad`; kolejka mieści całą falę naraz |

Rząd wielkości jest ten sam, ale w typowym labiryncie **fala jest znacznie
grubsza niż jedna trasa** — i to dlatego przy naprawdę dużych planszach sięga
się po nawroty, mimo że dają gorszą drogę. Zbiór `odwiedzone` w obu wersjach
zajmuje O(n) i nie da się go uniknąć: bez niego algorytm chodzi w kółko.

## Ćwiczenia

Pobierz szkielet z gotowymi testami. Uzupełniasz pięć funkcji plus szóstą
na ocenę wyższą, uruchamiasz plik i od razu widzisz, co przechodzi.

[:material-language-python: Szkielet z testami (.py)](../pliki/labirynt-szkielet.py){ .md-button .md-button--primary download="labirynt-szkielet.py" }

!!! note "Ćwiczenie 1. Na kartce, zanim usiądziesz do kodu"

    Weź labirynt z sekcji 1 i **zmień kolejność** sprawdzania sąsiadów na
    **dół → prawo → góra → lewo**. Poprowadź tabelkę stosu jak w sekcji 2.

    1. Ile nawrotów wykonał algorytm tym razem?
    2. Jaką drogę znalazł i ile ma pól?
    3. Czy wynik BFS się zmienił? Uzasadnij odpowiedź, nie sprawdzając programem.

    Punkt 3 jest najważniejszy: pokazuje, co w tych algorytmach jest przypadkiem,
    a co gwarancją.

!!! note "Ćwiczenie 2. Nawroty"

    Uzupełnij w szkielecie funkcje `sasiedzi` i `szukaj_rekurencyjnie`.
    Testy sprawdzają trzy rzeczy: że znaleziona droga zaczyna się w `S`
    i kończy w `E`, że kolejne pola drogi **sąsiadują ze sobą** i że dla
    labiryntu bez wyjścia funkcja zwraca `None`.

    Gdy działa, dopisz `licz_nawroty` — ta sama funkcja, tylko zliczająca,
    ile razy wykonano `droga.pop()`.

!!! note "Ćwiczenie 3. Najkrótsza droga"

    Uzupełnij `najkrotsza_droga` (kolejka) oraz `odtworz`. Testy sprawdzają nie
    tylko długość drogi, ale i to, czy kolejne pola naprawdę ze sobą sąsiadują —
    droga „przeskakująca" przez ścianę testu nie przejdzie.

    Na koniec uruchom `porownaj()` — wypisze tabelkę taką jak w sekcji 4 dla
    wszystkich labiryntów z pliku. Dla **jednego** z nich obie metody dają drogę
    tej samej długości. Znajdź go, obejrzyj i wyjaśnij, co takiego ma w sobie,
    że wynik nawrotów nie może tam być gorszy od najkrótszego.

!!! note "Ćwiczenie 4. Wersja iteracyjna nawrotów"

    Przepisz `szukaj_rekurencyjnie` na `szukaj_iteracyjnie` — bez rekurencji,
    z własnym stosem w liście. To ta sama logika, tylko zamiast wywołań
    odkładasz na stos pary „pole + które kierunki jeszcze zostały".

    Sprawdź na labiryncie budowanym funkcją `waz()` (długi kręty korytarz
    o blisko 1500 polach), że wersja rekurencyjna przewraca się na
    `RecursionError`, a iteracyjna przechodzi go w całości.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Który algorytm gwarantuje znalezienie najkrótszej drogi wyjścia z labiryntu?",
    "typ": "jedna",
    "opcje": [
      "Przeszukiwanie z nawrotami, bo cofa się ze ślepych zaułków",
      "Przeszukiwanie wszerz, bo używa kolejki",
      "Oba — różnią się tylko szybkością",
      "Żaden; najkrótszą drogę daje dopiero algorytm Dijkstry"
    ],
    "poprawna": 1,
    "wyjasnienie": "Kolejka obsługuje pola w kolejności rosnącej odległości od startu, więc wyjście wychodzi z niej dopiero wtedy, gdy krótsza droga do niego nie istnieje. Dijkstra jest potrzebny dopiero, gdy przejścia mają różne koszty."
  },
  {
    "pytanie": "Na czym dokładnie polega nawrót w przeszukiwaniu z nawrotami?",
    "typ": "jedna",
    "opcje": [
      "Na usunięciu pola ze zbioru odwiedzonych",
      "Na zdjęciu pola z drogi po tym, jak zawiodły wszystkie kierunki z tego pola",
      "Na powrocie do startu i rozpoczęciu poszukiwań od nowa",
      "Na zamianie stosu na kolejkę"
    ],
    "poprawna": 1,
    "wyjasnienie": "Nawrót cofa poszukiwania o jeden krok. Pole znika z drogi, ale zostaje w zbiorze odwiedzonych — inaczej algorytm wchodziłby w ten sam ślepy zaułek raz za razem."
  },
  {
    "pytanie": "Dlaczego kolejki nie należy budować na zwykłej liście, używając pop(0)?",
    "typ": "jedna",
    "opcje": [
      "Bo lista nie potrafi przechowywać krotek",
      "Bo pop(0) przesuwa wszystkie pozostałe elementy, więc kosztuje czas liniowy",
      "Bo pop(0) zdejmuje element z końca, a nie z początku",
      "Bo lista ma ograniczoną długość"
    ],
    "poprawna": 1,
    "wyjasnienie": "pop(0) działa w czasie proporcjonalnym do długości listy, więc cały algorytm robi się O(n²). collections.deque zdejmuje z początku w czasie stałym."
  },
  {
    "pytanie": "W wersji z nawrotami stos w każdej chwili zawiera:",
    "typ": "jedna",
    "opcje": [
      "Wszystkie odwiedzone pola",
      "Pola, które dopiero czekają na sprawdzenie",
      "Bieżącą drogę od startu do pola, na którym stoimy",
      "Najkrótszą drogę znalezioną do tej pory"
    ],
    "poprawna": 2,
    "wyjasnienie": "Dlatego w chwili dojścia do wyjścia droga jest już gotowa i nic nie trzeba odtwarzać. W BFS jest odwrotnie — kolejka drogą nie jest, więc potrzebna jest mapa „skąd”."
  },
  {
    "pytanie": "Po co w algorytmie BFS zapisuje się mapę skad?",
    "typ": "jedna",
    "opcje": [
      "Żeby nie odwiedzić pola dwa razy",
      "Żeby po dojściu do wyjścia odtworzyć drogę, idąc wstecz do startu",
      "Żeby policzyć, ile pól ma labirynt",
      "Żeby przyspieszyć zdejmowanie z kolejki"
    ],
    "poprawna": 1,
    "wyjasnienie": "Za niewchodzenie dwa razy odpowiada zbiór odwiedzonych. Mapa skad służy wyłącznie do odtworzenia trasy: od wyjścia cofamy się po zapisanych poprzednikach i odwracamy wynik."
  },
  {
    "pytanie": "Jaka jest złożoność czasowa obu algorytmów dla labiryntu o n polach?",
    "typ": "jedna",
    "opcje": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
    "poprawna": 2,
    "wyjasnienie": "Każde pole jest odwiedzane najwyżej raz, a przy każdym sprawdzamy stałą liczbę sąsiadów — czterech. Razem daje to liczbę operacji proporcjonalną do liczby pól."
  },
  {
    "pytanie": "Program z rekurencyjnym szukaniem drogi przerywa się z RecursionError na labiryncie 60 × 60. Co jest przyczyną?",
    "typ": "jedna",
    "opcje": [
      "Labirynt nie ma wyjścia",
      "Zbiór odwiedzonych przepełnił pamięć",
      "Głębokość zagnieżdżenia wywołań przekroczyła limit Pythona, bo jedno wywołanie odpowiada jednemu polu drogi",
      "Kolejka została zbudowana na liście zamiast na deque"
    ],
    "poprawna": 2,
    "wyjasnienie": "Domyślny limit to około 1000 zagnieżdżeń, a droga w takim labiryncie może być znacznie dłuższa. Podniesienie limitu odsuwa problem; usuwa go dopiero wersja iteracyjna z własnym stosem."
  },
  {
    "pytanie": "Zmieniasz kolejność sprawdzania sąsiadów z góra-prawo-dół-lewo na dół-lewo-góra-prawo. Co się zmieni?",
    "typ": "jedna",
    "opcje": [
      "Droga znaleziona przez nawroty może być inna; długość drogi z BFS pozostanie ta sama",
      "Obie drogi pozostaną takie same",
      "Obie drogi się zmienią",
      "BFS przestanie znajdować wyjście"
    ],
    "poprawna": 0,
    "wyjasnienie": "Nawroty zwracają pierwszą napotkaną drogę, więc zależą od kolejności kierunków. BFS zwraca drogę o minimalnej długości — konkretna trasa przy remisie może się zmienić, ale liczba pól nie."
  }
]
</script>
</div>

## Karta pracy

Wypełnij kartę na tej stronie, a potem pobierz gotowy dokument Worda i oddaj
go przez **Zadania domowe w dzienniku VULCAN**.

<div class="karta-pracy" data-karta="labirynt"></div>

## Na ocenę celującą

Wybierz jedno zadanie i opisz wyniki w karcie pracy.

**A. Labirynt z ważonymi przejściami.** Dołóż do siatki znak `~` oznaczający
błoto — wejście na takie pole kosztuje 3 ruchy zamiast jednego. Pokaż na
przykładzie, że BFS przestaje wtedy dawać najtańszą drogę, i popraw algorytm,
zastępując kolejkę **kolejką priorytetową** (`heapq`). Porównaj wynik obu wersji
na tym samym labiryncie.

**B. Wszystkie drogi bez powtórzeń.** Napisz funkcję, która wypisuje **wszystkie**
drogi z `S` do `E` nieodwiedzające żadnego pola dwa razy. Wykorzystaj nawroty
i zastanów się, czym różni się tu obsługa zbioru odwiedzonych. Sprawdź, ile
takich dróg ma labirynt z sekcji 4, i wyjaśnij, dlaczego przy większych
labiryntach ta liczba wybucha.

**C. Generator labiryntów.** Napisz funkcję tworzącą losowy labirynt o zadanych
wymiarach metodą drążenia korytarzy z nawrotami — tym samym algorytmem, którego
używasz do szukania drogi, tylko odwróconym: zamiast szukać przejść, wybijasz je
w litym bloku ścian. Sprawdź, że w tak zbudowanym labiryncie droga z `S` do `E`
jest **dokładnie jedna**, i wyjaśnij, dlaczego wtedy obie metody zwracają tę samą
trasę.

---

*Przeszukiwanie wszerz opisał w 1959 r. **Edward F. Moore**, szukając najkrótszej
drogi w labiryncie; niezależnie i wcześniej, bo w 1945 r., odkrył je
**Konrad Zuse**, ale jego pracy wtedy nie opublikowano. Przeszukiwanie w głąb
jest starsze — jako metodę rozwiązywania labiryntów opisał je w XIX wieku
francuski matematyk **Charles Pierre Trémaux**.*
