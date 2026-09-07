# Informatyka 1TT — strona z materiałami

Statyczna strona z materiałami do lekcji informatyki dla klasy 1TT (zakres
rozszerzony, technikum): teoria, ćwiczenia przy komputerze i zadania sprawdzające
z odpowiedziami. Zbudowana na MkDocs Material, publikowana na GitHub Pages.

## Co jest w środku

```
.
├── .github/workflows/
│   └── deploy.yml       # buduje stronę i publikuje na GitHub Pages
├── mkdocs.yml           # konfiguracja: nawigacja, motyw, rozszerzenia Markdown
├── requirements.txt     # zależności Pythona (wersja przypięta — patrz niżej)
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

## Uruchomienie — raz, na start

### 1. Repozytorium

```powershell
cd informatyka-1tt
git init -b main
git add .
git commit -m "Materialy informatyka 1TT"
gh repo create informatyka-1tt --public --source=. --push
```

Bez narzędzia `gh` załóż repozytorium przez stronę GitHuba, a zamiast ostatniej
linii wykonaj:

```powershell
git remote add origin https://github.com/JoziMate/informatyka-1tt.git
git push -u origin main
```

!!! Repozytorium musi być publiczne
    GitHub Pages działa z repozytoriów prywatnych dopiero w płatnych planach
    (Pro, Team, Enterprise). Na darmowym koncie repozytorium musi być publiczne.
    Dla tej strony to nie problem — nie ma w niej danych uczniów ani niczego
    poufnego, a materiały i tak mają być widoczne.

### 2. Włącz GitHub Pages

W repozytorium: **Settings → Pages → Build and deployment → Source** ustaw na
**GitHub Actions**.

To jedyny krok, którego workflow nie zrobi za ciebie. Bez niego budowanie
przejdzie, a wdrożenie zakończy się błędem.

### 3. Poczekaj na pierwszy przebieg

Zakładka **Actions** pokaże workflow *Publikacja strony*. Po jego zakończeniu
strona jest pod adresem:

```
https://JoziMate.github.io/informatyka-1tt/
```

Jeśli nazwiesz repozytorium inaczej, popraw `site_url`, `repo_url` i `repo_name`
w `mkdocs.yml` — inaczej mapa strony i przycisk „Edytuj tę stronę" będą wskazywać
w złe miejsce.

## Codzienna praca

Dopisujesz treść, wypychasz zmiany, strona przebudowuje się sama:

```powershell
git add .
git commit -m "Temat 3: nowe technologie"
git push
```

Przebieg trwa około minuty. Status widać w zakładce **Actions**; przy
niepowodzeniu GitHub wysyła powiadomienie mailem.

### Podgląd przed wypchnięciem

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Strona pojawi się na `http://127.0.0.1:8000` i przeładowuje się po każdym zapisie
pliku. To najwygodniejszy sposób pisania — Markdown w jednym oknie, efekt
w drugim.

## Jak dodać materiał do kolejnego tematu

1. Utwórz plik `.md` w katalogu odpowiedniego działu, np.
   `docs/dzial-1/sieci-komputerowe.md`.
2. Dopisz go do sekcji `nav:` w `mkdocs.yml` — inaczej budowanie ze flagą
   `--strict` zgłosi błąd, bo strona istnieje, ale nie ma do niej dojścia.
3. W `docs/index.md` zmień status tematu z *w przygotowaniu* na link.
4. `git add`, `git commit`, `git push`.

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

## Własna domena

W **Settings → Pages → Custom domain** wpisz adres, a u operatora domeny dodaj
rekord `CNAME` wskazujący na `jozimate.github.io`. GitHub sam wystawi certyfikat
HTTPS — zaznacz **Enforce HTTPS**, gdy stanie się dostępne. Po podpięciu domeny
zaktualizuj `site_url` w `mkdocs.yml`.

## Cztery rzeczy, o których warto wiedzieć

**Wersje akcji są przypięte do konkretnych wydań.** `deploy.yml` używa
`checkout@v7`, `setup-python@v6`, `configure-pages@v6`, `upload-pages-artifact@v5`
i `deploy-pages@v5` — sprawdzone jako aktualne we wrześniu 2026. GitHub wycofuje
stare wersje akcji, więc gdy za rok czy dwa workflow zacznie zgłaszać ostrzeżenia
o przestarzałych wersjach, wystarczy podbić numery.

**Wersja MkDocs Material też jest przypięta celowo.** Zespół Material zapowiedział,
że MkDocs 2.0 wprowadzi zmiany niekompatybilne wstecz — wtyczki i nadpisania
motywu przestaną działać, bez ścieżki migracji. Przypięta wersja sprawia, że
strona nie przestanie się budować w środku roku szkolnego. Aktualizuj świadomie,
poza sezonem.

**Budowanie działa w trybie `--strict`.** Każde ostrzeżenie — martwy odsyłacz,
strona spoza nawigacji — przerywa wdrożenie. To celowe: lepiej, żeby zmiana się
nie opublikowała, niż żeby uczniowie trafili na zepsuty link. Jeśli kiedyś będzie
przeszkadzać, usuń `--strict` z `.github/workflows/deploy.yml`.

**Wyszukiwarka nie odmienia polskich słów.** Biblioteka lunr, na której opiera się
wyszukiwanie w Material, nie ma polskiego stemmera. Szukanie działa, ale dopasowuje
formy dosłownie: „defragmentacja" znajdzie „defragmentacja", nie znajdzie
„defragmentacji". Przy stronie tej wielkości to nie problem.

## Licencja i treść

Materiały do użytku edukacyjnego PCEiKZ Szczucin. Treść lekcji jest napisana od
zera i nie przepisuje podręcznika; odsyła do niego jako do materiału
uzupełniającego. Zakres tematów wynika z podstawy programowej — dokumentu
publicznego.
