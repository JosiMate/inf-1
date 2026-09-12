# Nowe technologie i oprogramowanie

!!! abstract "O tym temacie"

    **1 godzina lekcyjna** · Dział I. Urządzenia komputerowe w sieci
    · podstawa programowa **III.1**, **III.2**

    Chmura, sztuczna inteligencja, internet rzeczy, druk 3D — słowa, które
    słyszysz codziennie i które w reklamach znaczą wszystko, czyli nic. Ta
    lekcja jest o tym, co się za nimi naprawdę kryje i jak ocenić nową
    technologię, zanim się jej zaufa: czyje to dane, kto płaci i co się stanie,
    gdy usługa zostanie wyłączona.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wymienić etapy rozwoju technologii komputerowych i wskazać, co napędzało każdy z nich
    2. wyjaśnić, czym jest chmura obliczeniowa, i rozróżnić modele IaaS, PaaS i SaaS
    3. wyjaśnić, czym jest sztuczna inteligencja i uczenie maszynowe, oraz wskazać ograniczenia tych rozwiązań
    4. podać zastosowania automatyki, robotyki, internetu rzeczy i druku 3D wraz z ich zaletami i ryzykami
    5. rozróżnić rodzaje licencji oprogramowania i sprawdzić, na jakiej licencji działa program, którego używasz
    6. ocenić nową technologię według stałego zestawu pytań, zamiast opierać się na reklamie

## Jak czytać tę stronę

Materiał jest ułożony narastająco. Sekcje oznaczone etykietami odpowiadają
poziomom wymagań — jeśli celujesz w ocenę dobrą lub wyższą, nie pomijaj ich.

| Etykieta | Poziom |
| --- | --- |
| bez etykiety | wymagania konieczne i podstawowe (oceny 2–3) |
| :material-plus-circle: **rozszerzenie** | wymagania rozszerzające (ocena 4) |
| :material-star: **dopełnienie** | wymagania dopełniające (ocena 5) |

---

## 1. Etapy rozwoju technologii komputerowych

Historia komputerów to nie ciąg coraz szybszych maszyn, tylko kilka momentów,
w których **zmieniło się to, do czego komputer w ogóle służy**.

| Etap | Czym się charakteryzował | Co zmienił |
| --- | --- | --- |
| Lampy elektronowe (lata 40.–50.) | maszyny wielkości sali, obliczenia wojskowe i naukowe | komputer liczy szybciej niż człowiek |
| Tranzystory (lata 50.–60.) | mniejsze, tańsze, mniej awaryjne | komputer trafia do firm i uczelni |
| Układy scalone (lata 60.–70.) | wiele tranzystorów w jednej kostce | spadek ceny, początek masowej produkcji |
| Mikroprocesory (od lat 70.) | cały procesor w jednym układzie | komputer osobisty, komputer w domu |
| Sieci i internet (od lat 90.) | komputery połączone ze sobą | wartością staje się dostęp do danych, nie sam sprzęt |
| Chmura i urządzenia mobilne (od ok. 2007) | moc obliczeniowa wynajmowana zdalnie, smartfon w kieszeni | komputer jest wszędzie i nie trzeba go mieć |
| Sztuczna inteligencja (od ok. 2012) | uczenie maszynowe na dużych zbiorach danych | komputer rozpoznaje wzorce, których nikt nie zaprogramował wprost |

**Prawo Moore'a** — sformułowana w 1965 r. obserwacja Gordona Moore'a, że liczba
tranzystorów w układzie scalonym podwaja się mniej więcej co dwa lata. Przez
pół wieku sprawdzało się zaskakująco dobrze, ale dziś tempo wyraźnie zwolniło:
tranzystory zbliżają się do rozmiarów pojedynczych atomów, a bariera przestała
być tylko techniczna — stała się też ekonomiczna. Dlatego wzrost wydajności
bierze się dziś raczej z **wielu rdzeni i układów wyspecjalizowanych** (GPU,
układy do obliczeń AI) niż z samego przyspieszania jednego procesora.

!!! question "Zastanów się"

    Który z etapów w tabeli zmienił najwięcej w **życiu codziennym**, a nie
    w samej technice? Uzasadnij — to pytanie wraca w karcie pracy.

---

## 2. Chmura obliczeniowa

**Chmura to cudzy komputer, który wynajmujesz na godziny.** Zamiast kupować
serwer, płacisz za moc obliczeniową, miejsce na dane albo gotową usługę —
i zwalniasz je, gdy przestają być potrzebne.

### Trzy modele usług

| Model | Co dostajesz | Czym się zajmujesz ty | Przykład |
| --- | --- | --- | --- |
| **IaaS** *(infrastruktura jako usługa)* | maszynę wirtualną, dysk, sieć | systemem, aplikacjami, kopiami | wynajęty serwer wirtualny |
| **PaaS** *(platforma jako usługa)* | gotowe środowisko do uruchomienia programu | tylko swoim programem | hosting aplikacji z bazą danych |
| **SaaS** *(oprogramowanie jako usługa)* | gotowy program w przeglądarce | tylko swoimi danymi | poczta w przeglądarce, dokumenty online |

Im niżej w tabeli, tym mniej masz pracy — i tym mniej kontroli.

### Modele wdrożenia

**Chmura publiczna** — zasoby dostawcy dzielone między wielu klientów; najtańsza.
**Chmura prywatna** — infrastruktura dedykowana jednej organizacji; droższa, ale
dane nie opuszczają jej środowiska. **Chmura hybrydowa** — połączenie obu:
dane wrażliwe zostają u siebie, reszta idzie do chmury publicznej.

!!! warning "Trzy pytania, zanim wrzucisz coś do chmury"

    1. **Gdzie fizycznie leżą dane?** Przy danych osobowych ma to znaczenie
       prawne — RODO reguluje przekazywanie danych poza Europejski Obszar Gospodarczy.
    2. **Co, jeśli nie będzie internetu?** Usługa w chmurze bez łącza to usługa,
       której nie ma.
    3. **Jak stamtąd wyjść?** Przeniesienie danych do innego dostawcy bywa
       kosztowne i czasochłonne — to zjawisko nazywa się **uzależnieniem od
       dostawcy** (*vendor lock-in*).

:material-plus-circle: **rozszerzenie** — **przetwarzanie brzegowe** (*edge
computing*) to odwrót od wysyłania wszystkiego do chmury: dane przetwarza się
blisko miejsca powstania (w kamerze, w bramce IoT, w samochodzie), a do chmury
trafia dopiero wynik. Zyskuje się czas reakcji i prywatność, traci — łatwość
centralnego zarządzania.

---

## 3. Sztuczna inteligencja

**Sztuczna inteligencja (AI)** to zbiorcza nazwa metod, dzięki którym program
wykonuje zadania wymagające zwykle ludzkiej inteligencji: rozpoznaje obraz,
tłumaczy tekst, podpowiada kolejne słowo.

**Uczenie maszynowe** (*machine learning*) to najczęściej dziś używane podejście:
programista **nie zapisuje reguł**, tylko podaje dużo przykładów, a program sam
wyszukuje w nich prawidłowości. Odmianą jest **uczenie głębokie** (*deep
learning*), oparte na sieciach neuronowych o wielu warstwach.

**Modele generatywne** tworzą nową treść — tekst, obraz, dźwięk, kod — na
podstawie wzorców z danych treningowych.

!!! danger "Czego model językowy nie robi"

    Nie sprawdza, czy to, co pisze, jest prawdą. Dobiera kolejne słowa tak, by
    tekst **wyglądał** poprawnie — dlatego potrafi z pełnym przekonaniem podać
    nieistniejący przepis prawa albo wymyślony wyrok. Nazywa się to
    **halucynacją** i nie jest usterką do naprawienia w kolejnej wersji, tylko
    konsekwencją sposobu działania.

    Wniosek praktyczny: **każdy fakt z AI weryfikujesz w źródle** — dokładnie
    tak samo, jak weryfikujesz wpis na forum.

Model uczy się z danych, które dostał. Jeśli dane były stronnicze, model
powtórzy to uprzedzenie — i zrobi to w sposób trudny do wykrycia, bo nikt nie
zapisał takiej reguły wprost.

### Co mówi prawo :material-plus-circle: **rozszerzenie**

Unijne rozporządzenie o sztucznej inteligencji (**AI Act**) wprowadza obowiązki
stopniowo. Od **2 sierpnia 2026 r.** obowiązują wymogi przejrzystości:

- użytkownik musi zostać poinformowany, **najpóźniej przy pierwszym kontakcie**,
  że rozmawia z systemem AI, a nie z człowiekiem;
- treści wygenerowane lub zmodyfikowane przez AI — w tym deepfake'i i teksty
  publikowane w sprawach interesu publicznego — muszą być **oznaczone**, również
  w formacie odczytywalnym maszynowo.

Kolejne terminy: **2 grudnia 2026 r.** — dostosowanie części systemów
generatywnych wprowadzonych przed sierpniem 2026; **2 grudnia 2027 r.** —
przepisy dla systemów wysokiego ryzyka; **2 sierpnia 2028 r.** — wymagania dla
AI wbudowanej w produkty objęte odrębnymi regulacjami.

---

## 4. Internet rzeczy

**Internet rzeczy (IoT)** to urządzenia codziennego użytku wyposażone w czujniki
i połączenie z siecią: opaska sportowa, termostat, licznik energii, czujnik
wilgotności w uprawie, kamera przy drzwiach.

| Zaleta | Cena, jaką się płaci |
| --- | --- |
| zdalny podgląd i sterowanie | urządzenie musi mieć dostęp do sieci |
| automatyczne reagowanie na pomiary | ktoś zbiera dane o twoim rytmie dnia |
| oszczędność energii i czasu | po wyłączeniu usługi sprzęt bywa bezużyteczny |

!!! danger "Najsłabsze ogniwo sieci domowej"

    Urządzenia IoT są tanie, a producent rzadko wspiera je latami. Typowy zestaw
    problemów: **domyślne hasło** (admin/admin), **brak aktualizacji**
    oprogramowania i otwarte usługi widoczne z internetu. Przejęta kamera bywa
    wejściem do całej sieci domowej.

    Minimum: zmienić hasło, włączyć automatyczne aktualizacje, a sprzęt, który
    nie musi być widoczny z internetu — odciąć od niego (np. wydzielona sieć
    dla gości).

---

## 5. Automatyka i robotyka

**Automatyka** zajmuje się sterowaniem procesami bez udziału człowieka — od
regulatora temperatury po linię produkcyjną. **Robotyka** dokłada do tego
maszynę zdolną do ruchu i wykonywania zadań fizycznych.

- **Roboty przemysłowe** — spawanie, malowanie, pakowanie; pracują w klatkach,
  bo są szybkie i silne.
- **Coboty** (roboty współpracujące) — projektowane do pracy obok człowieka,
  z ograniczoną siłą i czujnikami kolizji.
- **Wózki AGV/AMR** w magazynach — same rozwożą towar między regałami.
- **Roboty medyczne** — precyzyjne ramiona sterowane przez chirurga.
- **RPA** (*robotic process automation*) — „robot" programowy, który klika
  w aplikacjach za pracownika: przepisuje faktury, przenosi dane między systemami.

:material-star: **dopełnienie** — automatyzacja nie tyle likwiduje pracę, ile
**przesuwa jej rodzaj**: ubywa zadań powtarzalnych, przybywa obsługi,
programowania i nadzoru nad maszynami. Pytanie egzaminacyjne brzmi zwykle nie
„czy roboty zabiorą pracę", tylko **„które czynności w tym zawodzie da się
opisać regułami"** — bo to właśnie one automatyzują się najłatwiej.

---

## 6. Druk 3D

Drukarka 3D buduje przedmiot **warstwa po warstwie** z modelu przygotowanego
w programie CAD. Dwie najpopularniejsze techniki:

| Technika | Jak działa | Do czego |
| --- | --- | --- |
| **FDM** | topi i układa włókno z tworzywa | prototypy, części zamienne, nauka |
| **SLA / DLP** | utwardza światłem ciekłą żywicę | detale wymagające precyzji, modele dentystyczne |

**Zastosowania:** szybkie prototypowanie (dzień zamiast tygodni), części
zamienne do sprzętu, którego nikt już nie produkuje, protezy i implanty
dopasowane do pacjenta, formy odlewnicze, makiety architektoniczne.

**Ograniczenia:** wydruk trwa godziny, wytrzymałość jest niższa niż elementu
wtryskiwanego czy frezowanego, a jakość zależy od kalibracji. Dochodzi kwestia
prawna — model 3D jest utworem i podlega prawu autorskiemu, a druk niektórych
przedmiotów (części broni, elementy podlegające homologacji) jest zabroniony.

---

## 7. Rzeczywistość wirtualna i rozszerzona

| Skrót | Nazwa | Na czym polega |
| --- | --- | --- |
| **VR** | rzeczywistość wirtualna | świat w całości wygenerowany; gogle odcinają obraz realny |
| **AR** | rzeczywistość rozszerzona | obraz realny **plus** nałożone informacje (ekran telefonu, okulary) |
| **MR** | rzeczywistość mieszana | obiekty wirtualne reagują na realne otoczenie |

**Gdzie to naprawdę działa:** szkolenia w warunkach, w których błąd jest drogi
(pilotaż, chirurgia, praca pod napięciem), przymiarka mebla we własnym pokoju,
podgląd instrukcji serwisowej na sprzęcie, wizualizacja projektu przed budową.

**Gdzie zawodzi:** koszt sprzętu, choroba symulatorowa przy dłuższej sesji,
konieczność przygotowania treści — sam sprzęt bez materiałów jest bezużyteczny.

---

## 8. Oprogramowanie i licencje

Kupując program, zwykle **nie kupujesz programu** — kupujesz prawo do korzystania
z niego na warunkach zapisanych w licencji (**EULA**, umowa licencyjna
użytkownika końcowego). To ten ekran, który wszyscy przeklikują.

| Rodzaj | Co wolno | Na co uważać |
| --- | --- | --- |
| **Komercyjna** | to, co zapisano w umowie, po opłaceniu | licencja stanowiskowa, edukacyjna i firmowa to różne warunki |
| **Subskrypcja / SaaS** | korzystać, dopóki płacisz | po zakończeniu opłat program przestaje działać |
| **Freeware** | używać bezpłatnie | często tylko do użytku niekomercyjnego; kod źródłowy zamknięty |
| **Shareware / trial** | testować przez określony czas lub w ograniczonej wersji | po terminie trzeba kupić albo odinstalować |
| **Open source** (np. **GNU GPL**, **MIT**) | używać, badać, zmieniać i rozpowszechniać kod | GPL wymaga, by wersja pochodna też była na GPL (*copyleft*); MIT jest łagodniejsza |
| **Domena publiczna** | wszystko — prawa majątkowe wygasły lub zostały zrzeczone | dotyczy utworu, nie znaku towarowego |
| **Creative Commons** | zależnie od wariantu (BY, SA, NC, ND) | licencje dla treści: zdjęć, tekstów, muzyki — nie dla kodu |

!!! tip "Wolne oprogramowanie ≠ darmowe"

    Angielskie *free software* znaczy „wolne", nie „darmowe". Chodzi o cztery
    wolności: uruchamiania, badania, modyfikowania i rozpowszechniania programu.
    Za wolne oprogramowanie można pobierać opłaty — płaci się wtedy za nośnik,
    wsparcie albo wdrożenie, nie za samo prawo do użycia.

Gdzie szukać licencji w programie: menu **Pomoc → O programie**, plik
`LICENSE` lub `COPYING` w katalogu instalacyjnym, strona projektu.

---

## 9. Jak ocenić nową technologię

Zanim uznasz, że coś jest przełomem, zadaj pięć pytań. Te same pytania
zastosujesz w karcie pracy.

1. **Jaki problem to rozwiązuje?** Jeśli odpowiedź brzmi „to jest nowoczesne",
   problemu nie ma.
2. **Kto za to płaci?** Jeśli usługa jest darmowa, sprawdź, co jest towarem —
   zwykle dane albo uwaga użytkownika.
3. **Jakie dane zbiera i gdzie trafiają?** Kto ma do nich dostęp i na jak długo.
4. **Co się stanie, gdy to przestanie działać?** Dostawca zamyka usługę, kończy
   się subskrypcja, znika internet — czy zostaje ci cokolwiek.
5. **Kto odpowiada za błąd?** Gdy system podejmie złą decyzję, odpowiedzialność
   ponosi człowiek albo firma — nigdy „algorytm".

---

## Ćwiczenia

!!! note "Ćwiczenie 1. Karta technologii"

    Wybierz **jedną** technologię: chmura obliczeniowa, AI generatywna, IoT,
    robotyka, druk 3D albo AR/VR. Znajdź **konkretne** zastosowanie w wybranej
    dziedzinie (medycyna, rolnictwo, transport, edukacja, przemysł) — nie ogólnik,
    tylko opisany przypadek.

    Odpowiedz na pięć pytań z sekcji 9 i podaj **dwa źródła**: jedno polskie
    i jedno branżowe (dopuszczalne anglojęzyczne). Wynik zapisz w karcie
    pracy — zadanie 2.

!!! note "Ćwiczenie 2. Licencje programów w pracowni"

    Sprawdź licencje **trzech** programów zainstalowanych na twoim stanowisku
    (np. przeglądarka, archiwizator, edytor tekstu, program graficzny).

    Dla każdego ustal: pełną nazwę i wersję, rodzaj licencji, czy wolno go używać
    komercyjnie i gdzie tę informację znalazłeś. Wynik — zadanie 3 w karcie pracy.

!!! note "Ćwiczenie 3. Test na halucynację" :material-plus-circle: **rozszerzenie**

    Zadaj dowolnemu narzędziu AI pytanie z dziedziny, którą znasz dobrze —
    o przepis, datę, definicję albo parametr sprzętu. Sprawdź odpowiedź
    w źródle. Zapisz w karcie pracy: treść pytania, odpowiedź narzędzia, co mówi
    źródło i czy odpowiedź była poprawna, częściowo poprawna czy zmyślona.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Szkoła wynajmuje w chmurze gotowy dziennik elektroniczny działający w przeglądarce. Który to model usługi?",
    "typ": "jedna",
    "opcje": ["IaaS", "PaaS", "SaaS", "Chmura prywatna"],
    "poprawna": 2,
    "wyjasnienie": "Dostawca odpowiada za sprzęt, system, bazę i samą aplikację — szkoła wprowadza tylko dane. To oprogramowanie jako usługa (SaaS)."
  },
  {
    "pytanie": "Co oznacza „uzależnienie od dostawcy” (vendor lock-in)?",
    "typ": "jedna",
    "opcje": [
      "Usługa działa tylko wtedy, gdy dostawca ma serwery w Polsce",
      "Przeniesienie danych i procesów do innego dostawcy jest kosztowne albo technicznie trudne",
      "Program wymaga stałego połączenia z internetem",
      "Licencja zabrania używania konkurencyjnego oprogramowania"
    ],
    "poprawna": 1,
    "wyjasnienie": "Im głębiej dane i procesy wrastają w jedno środowisko, tym trudniej je stamtąd wyjąć. To pytanie zadaje się PRZED wdrożeniem, nie po."
  },
  {
    "pytanie": "Model językowy podaje sygnaturę wyroku sądu, której nie ma w bazie orzeczeń. Jak nazywa się to zjawisko i skąd wynika?",
    "typ": "jedna",
    "opcje": [
      "Błąd bazy danych — model pobrał złe źródło",
      "Halucynacja — model dobiera treść tak, by wyglądała poprawnie, i nie sprawdza prawdziwości",
      "Przeuczenie modelu na zbyt małym zbiorze",
      "Uszkodzenie pliku modelu, które naprawi aktualizacja"
    ],
    "poprawna": 1,
    "wyjasnienie": "Model generuje tekst wyglądający wiarygodnie, bo tak został nauczony. Weryfikacja faktów w źródle należy do człowieka."
  },
  {
    "pytanie": "Od 2 sierpnia 2026 r. AI Act nakazuje między innymi:",
    "typ": "jedna",
    "opcje": [
      "zakaz używania modeli generatywnych w szkołach",
      "informowanie użytkownika, że rozmawia z systemem AI, i oznaczanie treści wygenerowanych przez AI",
      "rejestrację każdego użytkownika narzędzi AI w urzędzie",
      "publikowanie danych treningowych wszystkich modeli"
    ],
    "poprawna": 1,
    "wyjasnienie": "To wymogi przejrzystości: informacja o kontakcie z AI najpóźniej przy pierwszym kontakcie oraz oznaczanie treści wygenerowanych lub zmodyfikowanych przez AI, również maszynowo."
  },
  {
    "pytanie": "Które zagrożenie jest najbardziej typowe dla urządzeń internetu rzeczy w sieci domowej?",
    "typ": "jedna",
    "opcje": [
      "Zbyt duże zużycie pasma przez transmisję wideo",
      "Domyślne hasła i brak aktualizacji, przez co urządzenie staje się wejściem do sieci",
      "Niezgodność z protokołem IPv6",
      "Konieczność zakupu osobnego routera dla każdego urządzenia"
    ],
    "poprawna": 1,
    "wyjasnienie": "Tanie urządzenie bez wsparcia producenta zostaje w sieci latami z fabrycznym hasłem. Przejęta kamera czy termostat są przyczółkiem do reszty sieci."
  },
  {
    "pytanie": "Program rozpowszechniany na licencji GNU GPL zmodyfikowałeś i chcesz udostępnić swoją wersję. Co musisz zrobić?",
    "typ": "jedna",
    "opcje": [
      "Nic — GPL pozwala na dowolne wykorzystanie bez warunków",
      "Udostępnić ją na tej samej licencji, wraz z kodem źródłowym",
      "Wykupić licencję komercyjną u autora",
      "Zmienić nazwę programu i usunąć informacje o autorach"
    ],
    "poprawna": 1,
    "wyjasnienie": "GPL jest licencją typu copyleft: wersja pochodna dziedziczy warunki oryginału, łącznie z obowiązkiem udostępnienia kodu. Licencja MIT takiego wymogu nie stawia."
  },
  {
    "pytanie": "Czym przetwarzanie brzegowe (edge computing) różni się od klasycznej chmury?",
    "typ": "jedna",
    "opcje": [
      "Dane przetwarza się blisko miejsca ich powstania, a do chmury trafia dopiero wynik",
      "Dane są szyfrowane, a w chmurze nie są",
      "Działa wyłącznie w sieciach 5G",
      "Nie wymaga żadnego serwera"
    ],
    "poprawna": 0,
    "wyjasnienie": "Zysk to czas reakcji i prywatność — dane nie muszą jechać przez pół świata. Kosztem jest trudniejsze zarządzanie wieloma rozproszonymi urządzeniami."
  },
  {
    "pytanie": "Aplikacja jest darmowa i nie wyświetla reklam. Które pytanie z listy oceny technologii zadasz w pierwszej kolejności?",
    "typ": "jedna",
    "opcje": [
      "Czy działa na moim systemie operacyjnym",
      "Kto za to płaci i jakie dane aplikacja zbiera",
      "Czy ma polską wersję językową",
      "Ile miejsca zajmuje na dysku"
    ],
    "poprawna": 1,
    "wyjasnienie": "Utrzymanie usługi kosztuje. Jeśli nie płacisz pieniędzmi ani nie oglądasz reklam, warto sprawdzić w polityce prywatności, co jest przedmiotem wymiany."
  }
]
</script>
</div>

---

## Karta pracy

Wypełnij kartę na tej stronie, a potem pobierz gotowy dokument Worda i oddaj go
przez **Zadania domowe w dzienniku VULCAN**.

<div class="karta-pracy" data-karta="nowe-technologie"></div>

---

## Na ocenę celującą

Wybierz jedno zadanie i przygotuj krótkie omówienie dla klasy.

1. **Opracowanie o wybranej nowej technologii na podstawie źródeł branżowych,
   w tym anglojęzycznych.** Wymagane: co to rozwiązuje, jak działa w zarysie
   technicznym, stan wdrożeń, koszty, ograniczenia. Minimum trzy źródła,
   z czego jedno anglojęzyczne i jedno starsze niż dwa lata — po to, by pokazać,
   co z zapowiedzi sprzed dwóch lat rzeczywiście się wydarzyło.

2. **Technologia, która nie wypaliła.** Wybierz rozwiązanie ogłaszane jako
   przełom, które nie weszło do powszechnego użytku (np. 3D w telewizorach,
   okulary Google Glass w pierwszej odsłonie, blockchain w handlu detalicznym).
   Ustal, co konkretnie zawiodło: technika, cena, prawo czy brak realnej potrzeby.

3. **Własne zastosowanie.** Zaproponuj sposób wykorzystania jednej z omawianych
   technologii w naszej szkole albo w gminie. Opisz: problem, rozwiązanie,
   potrzebny sprzęt i oprogramowanie, szacowany koszt oraz największe ryzyko.

4. **Porównanie licencji.** Zestaw GNU GPL v3 z licencją MIT: czym różnią się
   obowiązki osoby, która buduje na cudzym kodzie program komercyjny? Podaj po
   jednym znanym projekcie na każdej z licencji.

---

!!! info "Źródła i materiały uzupełniające"

    - Terminy stosowania AI Act: [Ministerstwo Cyfryzacji — AI Act, co się zmieniło 2 sierpnia 2026](https://www.gov.pl/web/cyfryzacja/ai-act--co-sie-zmienilo-2-sierpnia-2026-roku)
    - Definicja wolnego oprogramowania i czterech wolności: [GNU — What is Free Software?](https://www.gnu.org/philosophy/free-sw.html)
    - Podręcznik: *Informatyka na czasie* — zakres rozszerzony, część 1, dział I

*Stan prawny i faktograficzny sprawdzony 12 września 2026 r.*
