# Informatyka 1TT — strona z materiałami

Statyczna strona z materiałami do lekcji informatyki dla klasy 1TT (zakres
rozszerzony, technikum): teoria, ćwiczenia przy komputerze i zadania sprawdzające
z odpowiedziami. Zbudowana na MkDocs Material, wdrażana na Vercel.

## Co jest w środku

```
.
├── mkdocs.yml           # konfiguracja: nawigacja, motyw, rozszerzenia Markdown
├── requirements.txt     # zależności Pythona (wersja przypięta — patrz niżej)
├── vercel.json          # komendy budowania dla Vercela
└── docs/
    ├── index.md                        # spis wszystkich 38 tematów
    ├── dzial-1/
    │   └── systemy-operacyjne.md       # gotowy materiał (temat 2, 2 godz.)
    └── assets/
        ├── extra.css                   # korekty stylu + reguły wydruku
        └── favicon.png
```

Strona główna wypisuje wszystkie tematy z rozkładu 1TT i oznacza, które mają już
materiały. Dodając nowy temat, pamiętaj o zmianie jego statusu w tej tabeli.

## Podgląd na własnym komputerze

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Strona pojawi się na `http://127.0.0.1:8000` i przeładowuje się sama po każdym
zapisie pliku. To najwygodniejszy sposób pisania — piszesz w Markdownie
w jednym oknie, widzisz efekt w drugim.

## Wdrożenie na Vercel

1. Wypchnij repozytorium na GitHub.
2. Na [vercel.com](https://vercel.com) wybierz **Add New → Project** i zaimportuj
   to repozytorium.
3. **Nie zmieniaj niczego w ustawieniach budowania.** Plik `vercel.json` już
   zawiera komplet:

   | Ustawienie | Wartość |
   | --- | --- |
   | Install Command | `python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt` |
   | Build Command | `python3 -m mkdocs build --strict` |
   | Output Directory | `site` |
   | Framework Preset | brak (Other) |

4. Kliknij **Deploy**.

Od tej pory każdy `git push` do gałęzi głównej automatycznie przebudowuje stronę.
Pushe na inne gałęzie dostają własny adres podglądowy — wygodne, gdy chcesz
zobaczyć zmiany przed pokazaniem ich uczniom.

### Jeśli budowanie na Vercelu się wysypie

Vercel buduje na Amazon Linux i sam wybiera wersję Pythona, więc czasem potrafi
zignorować przypięcia wersji. Gdyby instalacja zależności zaczęła się sypać,
jest pewny plan awaryjny — zbuduj stronę u siebie i pozwól Vercelowi tylko ją
serwować:

1. usuń `site/` z `.gitignore`,
2. lokalnie wykonaj `mkdocs build` i zacommituj katalog `site/`,
3. w ustawieniach projektu na Vercelu wyczyść **Install Command** i
   **Build Command**, a **Output Directory** ustaw na `site`.

Tracisz automatyczne budowanie (trzeba pamiętać o `mkdocs build` przed
commitem), ale wdrożenie przestaje zależeć od środowiska Vercela.

## Jak dodać materiał do kolejnego tematu

1. Utwórz plik `.md` w katalogu odpowiedniego działu, np.
   `docs/dzial-1/sieci-komputerowe.md`.
2. Dopisz go do sekcji `nav:` w `mkdocs.yml` — inaczej budowanie ze flagą
   `--strict` zgłosi błąd, bo strona istnieje, ale nie ma do niej dojścia.
3. W `docs/index.md` zmień status tematu z *w przygotowaniu* na link.
4. `git add`, `git commit`, `git push` — Vercel zrobi resztę.

### Konwencje przyjęte w gotowym materiale

Warto je powtarzać, żeby kolejne tematy czytało się tak samo. Wzorzec znajdziesz
w `docs/dzial-1/systemy-operacyjne.md`.

- **Ramka „O tym temacie"** na początku: liczba godzin, dział, zapisy podstawy
  programowej i jedno zdanie o tym, po co uczniowi ta lekcja.
- **Etykiety poziomów** przy sekcjach wykraczających poza podstawę:
  `:material-plus-circle: **rozszerzenie**` (ocena 4) oraz
  `:material-star: **dopełnienie**` (ocena 5). Sekcje bez etykiety to wymagania
  konieczne i podstawowe.
- **Ćwiczenia** numerowane, z nagłówkiem `### :material-console: Ćwiczenie N — …`
  i jasno wskazanym efektem („zapisz w zeszycie…").
- **Zadania sprawdzające** jako zwijane bloki `??? question "…"` z odpowiedzią
  w środku — uczeń widzi pytanie, odpowiedź odsłania sam.
- **Sekcja „Na ocenę celującą"** z zadaniami wykraczającymi poza program.

Przydatne elementy Material, których konfiguracja już jest gotowa:

````markdown
!!! note "Ramka informacyjna"
    Treść ramki.

??? tip "Ramka zwijana — domyślnie schowana"
    Dobra na rozwiązania zadań.

```cpp
// bloki kodu z podświetlaniem i przyciskiem kopiowania
int main() { return 0; }
```

=== "Wariant A"
    Treść pierwszej zakładki.
=== "Wariant B"
    Treść drugiej zakładki.
````

## Trzy rzeczy, o których warto wiedzieć

**Wersja jest przypięta celowo.** `requirements.txt` wskazuje konkretną wersję
`mkdocs-material`. Zespół Material zapowiedział, że MkDocs 2.0 wprowadzi zmiany
niekompatybilne wstecz — wtyczki i nadpisania motywu przestaną działać, bez
ścieżki migracji. Przypięta wersja sprawia, że strona nie przestanie się budować
w środku roku szkolnego. Aktualizuj świadomie, poza sezonem.

**Budowanie działa w trybie `--strict`.** Każde ostrzeżenie — martwy odsyłacz,
strona spoza nawigacji — przerywa wdrożenie i Vercel przyśle powiadomienie
o nieudanym buildzie. To celowe: lepiej, żeby zmiana się nie opublikowała, niż
żeby uczniowie trafili na zepsuty link. Jeśli kiedyś będzie przeszkadzać, usuń
`--strict` z `vercel.json`.

**Wyszukiwarka nie odmienia polskich słów.** Biblioteka lunr, na której opiera
się wyszukiwanie w Material, nie ma polskiego stemmera. Szukanie działa, ale
dopasowuje formy dosłownie: „wymagania" znajdzie „wymagania", nie znajdzie
„wymaganiom". Przy stronie tej wielkości to nie problem.

## Licencja i treść

Materiały do użytku edukacyjnego PCEiKZ Szczucin. Treść lekcji jest napisana od
zera i nie przepisuje podręcznika; odsyła do niego jako do materiału
uzupełniającego. Zakres tematów wynika z podstawy programowej — dokumentu
publicznego.
