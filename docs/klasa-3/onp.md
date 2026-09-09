# Odwrotna notacja polska (ONP)

!!! abstract "O tym temacie"

    **4 godziny lekcyjne** · Dział II. Rozwiązywanie problemów z wykorzystaniem
    dynamicznych struktur danych · podstawa programowa **I.1, I.3, RI.2, RI.3,
    RI.5, RI.10, II.1, RII.2**

    Pierwszy temat, w którym struktura danych jest ważniejsza od samego
    algorytmu. Cały problem — obliczanie wyrażeń z nawiasami i priorytetami —
    rozwiązuje się jednym przebiegiem, jeśli tylko ma się **stos**.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. zapisać wyrażenie w odwrotnej notacji polskiej i wyjaśnić, dlaczego nie potrzebuje ono nawiasów
    2. obliczyć wartość wyrażenia w ONP, prowadząc tabelę stanu stosu
    3. wymienić operacje na stosie i zrealizować je na liście w Pythonie
    4. zaimplementować kalkulator ONP i wyjaśnić, dlaczego przy odejmowaniu i dzieleniu kolejność zdejmowania ze stosu ma znaczenie
    5. zaimplementować algorytm stacji rozrządowej zamieniający zapis tradycyjny na ONP
    6. uwzględnić w algorytmie priorytet i łączność operatorów, w tym prawostronną łączność potęgowania
    7. uzasadnić liniową złożoność obu algorytmów, odwołując się do liczby operacji na stosie

## 1. Skąd wziął się problem

Zapis `2 + 3 * 4` jest dla człowieka oczywisty, dla programu — nie. Żeby go
policzyć, trzeba znać **priorytety** działań, **łączność** operatorów i umieć
rozwikłać **nawiasy**. Komputer czyta wyrażenie od lewej do prawej i w chwili,
gdy widzi `+`, jeszcze nie wie, czy wolno mu dodawać — bo dalej może stać `*`.

Odwrotna notacja polska usuwa ten problem u źródła: **operator stoi za swoimi
argumentami**, więc nawiasy przestają być potrzebne, a kolejność działań wynika
wprost z kolejności zapisu.

| Zapis | Nazwa | Przykład |
| --- | --- | --- |
| `2 + 3` | infiksowy — operator w środku | zwykły zapis szkolny |
| `+ 2 3` | prefiksowy — **notacja polska** | operator przed argumentami |
| `2 3 +` | sufiksowy — **odwrotna notacja polska** | operator po argumentach |

!!! info "Skąd nazwa"

    Notację prefiksową wymyślił w **1924 roku** polski logik **Jan Łukasiewicz** —
    stąd „notacja polska". Wersję sufiksową rozwinęli w latach pięćdziesiątych
    i sześćdziesiątych między innymi **Charles Hamblin**, **Friedrich Bauer**
    i **Edsger Dijkstra**, na potrzeby maszynowego obliczania wyrażeń.

    Do powszechnej świadomości ONP trafiła w **1972 roku** wraz z kalkulatorem
    **HP-35** — pierwszym naukowym kalkulatorem kieszonkowym. Kalkulatory
    z ONP nie mają klawisza `=`; zamiast niego jest `ENTER`, którym odkłada się
    liczbę na stos. Inżynierowie do dziś się o nie kłócą.

### Drzewo wyrażenia

Wszystkie trzy zapisy to ten sam obiekt oglądany z innej strony — **drzewo
wyrażenia**. Operatory są w węzłach, liczby w liściach:

```text
        *
       / \
      +   4
     / \
    2   3
```

- obejdź drzewo **korzeń → lewo → prawo** i dostaniesz zapis prefiksowy: `* + 2 3 4`
- obejdź **lewo → korzeń → prawo** i dostaniesz infiksowy: `2 + 3 * 4`
- obejdź **lewo → prawo → korzeń** i dostaniesz ONP: `2 3 + 4 *`

Zauważ, że to drzewo odpowiada wyrażeniu `(2 + 3) * 4`. Zapis infiksowy bez
nawiasów jest **niejednoznaczny** — dopiero priorytety mówią, jak go czytać.
ONP i notacja polska niejednoznaczne nie są nigdy.

## 2. Stos — struktura, na której to stoi

**Stos** to dynamiczna struktura danych działająca według zasady **LIFO**
(*last in, first out*) — ostatni włożony element wychodzi pierwszy. Jak stos
talerzy: dokładasz na wierzch i z wierzchu zdejmujesz.

Cztery operacje wystarczą:

| Operacja | Co robi | W Pythonie |
| --- | --- | --- |
| `push` | odkłada element na wierzch | `stos.append(x)` |
| `pop` | zdejmuje i zwraca element z wierzchu | `stos.pop()` |
| `peek` / `top` | podgląda wierzch, nie zdejmując | `stos[-1]` |
| `isEmpty` | sprawdza, czy stos jest pusty | `not stos` |

W Pythonie stosem jest zwykła **lista** — `append` i `pop` bez argumentu działają
dokładnie na jej końcu, w czasie stałym. Nie trzeba niczego importować.

!!! warning "Lista to stos tylko wtedy, gdy używasz jej jak stosu"

    `pop()` bez argumentu zdejmuje z końca — to jest operacja stosowa.
    `pop(0)` zdejmuje z początku i **przesuwa całą resztę**, więc kosztuje
    czas proporcjonalny do długości listy. Jeśli potrzebujesz kolejki (FIFO),
    użyj `collections.deque`, a nie listy.

## 3. Obliczanie wartości wyrażenia w ONP

Algorytm mieści się w trzech zdaniach:

1. Czytaj symbole od lewej do prawej.
2. **Liczba** → odłóż ją na stos.
3. **Operator** → zdejmij dwa elementy, wykonaj działanie, wynik odłóż na stos.

Po przeczytaniu całego wyrażenia na stosie zostaje dokładnie jedna liczba — wynik.

Prześledźmy `5 1 2 + 4 * + 3 -`:

| Krok | Symbol | Działanie | Stos po kroku |
| :---: | :---: | --- | --- |
| 1 | `5` | odłóż | `[5]` |
| 2 | `1` | odłóż | `[5, 1]` |
| 3 | `2` | odłóż | `[5, 1, 2]` |
| 4 | `+` | 1 + 2 = 3 | `[5, 3]` |
| 5 | `4` | odłóż | `[5, 3, 4]` |
| 6 | `*` | 3 · 4 = 12 | `[5, 12]` |
| 7 | `+` | 5 + 12 = 17 | `[17]` |
| 8 | `3` | odłóż | `[17, 3]` |
| 9 | `-` | 17 − 3 = 14 | `[14]` |

!!! danger "Kolejność argumentów przy odejmowaniu i dzieleniu"

    Pierwszy zdjęty element to **prawy** argument działania:

    ```python
    b = stos.pop()      # prawy
    a = stos.pop()      # lewy
    stos.append(a - b)  # NIE b - a
    ```

    Przy `+` i `*` pomyłka nie boli, bo są przemienne. Przy `-` i `/` daje zły
    wynik — i to jest najczęstszy błąd w tym zadaniu.

## 4. Zamiana zapisu tradycyjnego na ONP

Algorytm nazywa się **stacją rozrządową** (*shunting-yard*) — Dijkstra porównał
go do kolejowej stacji rozrządowej, na której wagoniki są odstawiane na bocznicę
i podpinane w innej kolejności. Bocznicą jest stos operatorów.

=== "Reguły"

    - **liczba** → od razu do wyniku;
    - **operator** → dopóki na szczycie stosu stoi operator o **wyższym**
      priorytecie (albo **równym**, gdy bieżący jest lewostronny), przenoś go
      ze stosu do wyniku; potem odłóż bieżący operator na stos;
    - **nawias otwierający** → odłóż na stos;
    - **nawias zamykający** → przenoś ze stosu do wyniku, aż natrafisz na nawias
      otwierający; nawias otwierający usuń, do wyniku nie trafia;
    - **koniec wejścia** → przenieś do wyniku wszystko, co zostało na stosie.

=== "Priorytety i łączność"

    | Operator | Priorytet | Łączność |
    | :---: | :---: | --- |
    | `^` | 3 | **prawostronna** |
    | `*` `/` | 2 | lewostronna |
    | `+` `-` | 1 | lewostronna |

    Łączność decyduje w sytuacji remisu priorytetów:

    - `10 - 4 - 3` to `(10 - 4) - 3 = 3`, a nie `10 - (4 - 3) = 9`;
    - `2 ^ 3 ^ 2` to `2 ^ (3 ^ 2) = 512`, a nie `(2 ^ 3) ^ 2 = 64`.

    To jedyne miejsce algorytmu, w którym potęgowanie zachowuje się inaczej
    niż reszta — i jedyne, o które warto zapytać na sprawdzianie.

=== "Ślad dla `3 + 4 * 2`"

    | Symbol | Stos operatorów | Wynik |
    | :---: | --- | --- |
    | `3` | | `3` |
    | `+` | `+` | `3` |
    | `4` | `+` | `3 4` |
    | `*` | `+ *` | `3 4` |
    | `2` | `+ *` | `3 4 2` |
    | koniec | | `3 4 2 * +` |

    `*` nie wypchnęło `+` ze stosu, bo ma **wyższy** priorytet — dlatego trafia
    do wyniku wcześniej.

## 5. Złożoność

Każdy symbol wejścia jest odkładany na stos i zdejmowany **najwyżej raz**, więc
oba algorytmy wykonują liczbę operacji proporcjonalną do długości wyrażenia:
**złożoność liniowa, O(n)**. Pamięć w najgorszym przypadku też jest liniowa —
tyle zajmie stos dla wyrażenia w rodzaju `( ( ( ( 1 + 2 ) ) ) )`.

To jest powód, dla którego kompilatory i kalkulatory naukowe robią to właśnie
tak, a nie przez wielokrotne przeglądanie wyrażenia w poszukiwaniu najgłębszego
nawiasu.

## Ćwiczenia

Pobierz szkielet z gotowymi testami. Uzupełniasz trzy funkcje, uruchamiasz plik
i od razu widzisz, co przechodzi.

[:material-language-python: Szkielet z testami (.py)](../pliki/onp-szkielet.py){ .md-button .md-button--primary download="onp-szkielet.py" }

!!! note "Ćwiczenie 1. Na kartce, zanim usiądziesz do kodu"

    Policz na piechotę, prowadząc tabelkę stanu stosu jak w sekcji 3:

    1. `7 2 3 * -`
    2. `4 5 + 2 /`
    3. `2 3 4 ^ ^`

    Potem zamień na ONP, prowadząc tabelkę jak w sekcji 4:

    4. `( 8 - 3 ) * 2`
    5. `6 + 4 / 2 - 1`
    6. `3 ^ 2 ^ 2`

    Dopiero mając wyniki na kartce, sprawdź je programem. Kolejność jest
    celowa — na sprawdzianie i na maturze nie ma interpretera.

!!! note "Ćwiczenie 2. Kalkulator ONP"

    Uzupełnij w szkielecie funkcję `oblicz_onp`. Wszystkie pięć testów
    ma przechodzić, łącznie z tym o odejmowaniu i dzieleniu.

    Gdy działa, dopisz funkcję `slad_obliczen`, która zwraca listę stanów
    stosu po każdym kroku. To ta sama pętla, tylko zapamiętująca kopię stosu —
    zwróć uwagę, że `kroki.append(stos)` zapisze **odwołanie** do tej samej
    listy i wszystkie kroki wyjdą identyczne. Potrzebna jest kopia: `list(stos)`.

!!! note "Ćwiczenie 3. Stacja rozrządowa"

    Uzupełnij funkcję `na_onp`. Zacznij od wyrażeń bez nawiasów, potem dołóż
    obsługę nawiasów, a na końcu zajmij się łącznością potęgowania — testy
    `2 ^ 3 ^ 2` i `10 - 4 - 3` sprawdzają dokładnie to.

    Kiedy komplet dwunastu testów świeci na zielono, złóż obie funkcje razem
    i policz `( 12 + 4 ) * 3 - 10 / 5` jednym poleceniem.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Ile wynosi wyrażenie 7 2 3 * - zapisane w ONP?",
    "typ": "jedna",
    "opcje": ["1", "15", "-1", "12"],
    "poprawna": 0,
    "wyjasnienie": "Najpierw 2 · 3 = 6, potem 7 − 6 = 1. Operator działa na dwóch ostatnio odłożonych wartościach."
  },
  {
    "pytanie": "Jak zapisać ( 3 + 5 ) * 2 w odwrotnej notacji polskiej?",
    "typ": "jedna",
    "opcje": ["3 5 + 2 *", "3 5 2 * +", "* + 3 5 2", "3 + 5 2 *"],
    "poprawna": 0,
    "wyjasnienie": "Nawias wymusza dodawanie jako pierwsze, więc 3 5 + trafia do wyniku przed mnożeniem. W ONP nawiasy znikają — kolejność zapisu sama je zastępuje."
  },
  {
    "pytanie": "Która zasada opisuje działanie stosu?",
    "typ": "jedna",
    "opcje": [
      "FIFO — pierwszy włożony wychodzi pierwszy",
      "LIFO — ostatni włożony wychodzi pierwszy",
      "Elementy wychodzą w kolejności rosnącej",
      "Dostęp do dowolnego elementu przez indeks"
    ],
    "poprawna": 1,
    "wyjasnienie": "LIFO, last in — first out. FIFO opisuje kolejkę, a nie stos."
  },
  {
    "pytanie": "Obliczasz 8 3 - w Pythonie. Pierwszy zdjęty ze stosu element to:",
    "typ": "jedna",
    "opcje": [
      "8 — lewy argument odejmowania",
      "3 — prawy argument odejmowania",
      "Zależy od implementacji stosu",
      "Oba naraz, przez rozpakowanie krotki"
    ],
    "poprawna": 1,
    "wyjasnienie": "Stos zwraca ostatnio odłożony element, czyli 3. Dlatego trzeba zapisać a - b, gdzie b zdjęto jako pierwsze — odwrotna kolejność da -5 zamiast 5."
  },
  {
    "pytanie": "Ile wynosi 2 ^ 3 ^ 2 przy standardowej łączności potęgowania?",
    "typ": "jedna",
    "opcje": ["64", "512", "128", "36"],
    "poprawna": 1,
    "wyjasnienie": "Potęgowanie łączy się w prawo: 2 ^ (3 ^ 2) = 2 ^ 9 = 512. Gdyby łączyło się w lewo jak odejmowanie, wyszłoby (2 ^ 3) ^ 2 = 64."
  },
  {
    "pytanie": "W algorytmie stacji rozrządowej trafiasz na nawias zamykający. Co robisz?",
    "typ": "jedna",
    "opcje": [
      "Dopisujesz go do wyniku i idziesz dalej",
      "Odkładasz go na stos operatorów",
      "Przenosisz ze stosu do wyniku wszystko aż do nawiasu otwierającego, po czym ten nawias usuwasz",
      "Kończysz działanie algorytmu"
    ],
    "poprawna": 2,
    "wyjasnienie": "Nawiasy w ONP nie występują — służą tylko do wymuszenia kolejności, więc oba znikają, a operatory z ich wnętrza trafiają do wyniku wcześniej."
  },
  {
    "pytanie": "Jaka jest złożoność czasowa obliczania wyrażenia w ONP dla n symboli?",
    "typ": "jedna",
    "opcje": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
    "poprawna": 2,
    "wyjasnienie": "Każdy symbol jest odkładany i zdejmowany najwyżej raz, a to są operacje stałego czasu — razem daje to jeden przebieg przez wejście."
  },
  {
    "pytanie": "Dlaczego w Pythonie do implementacji stosu wystarczy zwykła lista?",
    "typ": "jedna",
    "opcje": [
      "Bo append i pop bez argumentu działają na końcu listy w czasie stałym",
      "Bo lista automatycznie sortuje elementy",
      "Bo lista ma wbudowaną metodę push",
      "Bo lista przechowuje wyłącznie liczby"
    ],
    "poprawna": 0,
    "wyjasnienie": "Koniec listy to naturalny wierzch stosu. Uwaga na pop(0) — zdejmowanie z początku przesuwa całą resztę i psuje złożoność."
  }
]
</script>
</div>

## Karta pracy

Wypełnij kartę na tej stronie, a potem pobierz gotowy dokument Worda i oddaj
go przez **Zadania domowe w dzienniku VULCAN**.

<div class="karta-pracy" data-karta="onp"></div>

## Na ocenę celującą

Wybierz jedno zadanie i opisz wyniki w karcie pracy.

**A. Kalkulator z kontrolą błędów.** Rozbuduj `oblicz_onp` tak, żeby rozpoznawał
niepoprawne wyrażenia i mówił, co jest nie tak: za mało argumentów dla operatora,
nadmiarowa liczba na stosie po zakończeniu, dzielenie przez zero, nieznany symbol.
Dla każdego przypadku podaj wyrażenie testowe i komunikat, który zwraca program.

**B. Notacja prefiksowa.** Napisz funkcję obliczającą wyrażenie w **notacji
polskiej** (`* + 2 3 4`). Wyjaśnij, dlaczego wygodnie jest czytać wejście
od prawej do lewej, i czym różni się obsługa argumentów w porównaniu z ONP.

**C. Drzewo wyrażenia.** Napisz funkcję, która z zapisu w ONP buduje drzewo
wyrażenia (na przykład jako zagnieżdżone krotki), a potem odtwarza z niego zapis
infiksowy z minimalną liczbą nawiasów — takich, bez których wyrażenie zmieniłoby
wartość. Pokaż to na `2 3 + 4 *` i na `2 3 4 * +`.

---

*Historia notacji: notację prefiksową wprowadził Jan Łukasiewicz w 1924 r.;
wersję sufiksową rozwinęli w latach 50. i 60. m.in. Charles Hamblin, Friedrich
Bauer i Edsger Dijkstra. Algorytm stacji rozrządowej pochodzi od Dijkstry.
Kalkulator HP-35 (1972) upowszechnił ONP wśród inżynierów.*
