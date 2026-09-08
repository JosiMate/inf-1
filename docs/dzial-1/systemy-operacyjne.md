# Systemy operacyjne w środowisku sieciowym

!!! abstract "O tym temacie"

    **2 godziny lekcyjne** · Dział I. Urządzenia komputerowe w sieci
    · podstawa programowa **III.3**, **V.3**

    Po tych zajęciach powinieneś umieć powiedzieć, co system operacyjny robi,
    kiedy go nie widzisz — i umieć sprawdzić w swoim komputerze rzeczy, o które
    dotąd nikt cię nie pytał: jaki ma system plików, czy warto go defragmentować
    i co się stanie, gdy nie uruchomi się rano przed sprawdzianem.

## Jak czytać tę stronę

Materiał jest ułożony narastająco. Sekcje oznaczone etykietami odpowiadają
poziomom wymagań — jeśli celujesz w ocenę dobrą lub wyższą, nie pomijaj ich.

| Etykieta | Poziom |
| --- | --- |
| bez etykiety | wymagania konieczne i podstawowe (oceny 2–3) |
| :material-plus-circle: **rozszerzenie** | wymagania rozszerzające (ocena 4) |
| :material-star: **dopełnienie** | wymagania dopełniające (ocena 5) |

---

## 1. Po co komputerowi system operacyjny

Uruchamiasz przeglądarkę i grę jednocześnie. Oba programy chcą procesora, pamięci
i dostępu do dysku. Żaden z nich nie wie o istnieniu drugiego. Ktoś musi
rozstrzygnąć, który dostanie procesor w najbliższej milisekundzie — i zrobić to
tak, żebyś nie zauważył, że w ogóle była o co walka.

Tym kimś jest **system operacyjny**: oprogramowanie pośredniczące między sprzętem
a programami użytkowymi.

### Pięć zadań, które wykonuje

**Zarządzanie procesami.** Przydziela czas procesora uruchomionym programom
i przełącza się między nimi tak szybko, że sprawiają wrażenie działających
równocześnie.

**Zarządzanie pamięcią.** Przydziela programom obszary pamięci RAM i pilnuje, by
jeden program nie zapisał czegoś w pamięci drugiego. Gdy RAM się kończy, przenosi
rzadziej używane dane na dysk (plik wymiany).

**Zarządzanie urządzeniami.** Rozmawia z drukarką, kartą sieciową i dyskiem za
pomocą **sterowników** — program użytkowy nie musi wiedzieć, jakiego modelu
drukarki używasz.

**Zarządzanie plikami.** Utrzymuje strukturę katalogów, pilnuje uprawnień
i decyduje, gdzie fizycznie na dysku wylądują twoje dane.

**Interfejs użytkownika.** Daje ci sposób wydawania poleceń — graficzny (okna,
ikony) albo tekstowy (wiersz poleceń).

### Przykłady systemów operacyjnych

| Przeznaczenie | Przykłady |
| --- | --- |
| komputery osobiste | Windows 11, macOS, Ubuntu, Fedora |
| serwery | Windows Server, Debian, Red Hat Enterprise Linux |
| urządzenia mobilne | Android, iOS |
| systemy wbudowane | FreeRTOS, Zephyr, Linux w routerach i telewizorach |

!!! question "Zastanów się"

    Router w twoim domu ma system operacyjny. Bankomat też. Czym te systemy
    różnią się od Windowsa pod względem zadań, które muszą wykonać?

---

## 2. Jądro systemu i tryby pracy

:material-star: **dopełnienie**

**Jądro** (ang. *kernel*) to najważniejsza część systemu operacyjnego — ta, która
faktycznie zarządza procesorem, pamięcią i urządzeniami. Reszta systemu to
programy działające *na* jądrze.

Procesor potrafi pracować w co najmniej dwóch trybach:

**Tryb jądra** (*kernel mode*) — kod ma pełny dostęp do sprzętu i całej pamięci.
Może wszystko, łącznie z zawieszeniem całego komputera.

**Tryb użytkownika** (*user mode*) — kod ma dostęp tylko do przydzielonej mu
pamięci. Gdy program się wysypie, ginie tylko on; system działa dalej.

### W jakim trybie pracuje sterownik urządzenia?

**W większości systemów operacyjnych sterowniki działają w trybie jądra.** Muszą
sięgać bezpośrednio do rejestrów urządzenia i obsługiwać przerwania sprzętowe,
a tego z trybu użytkownika zrobić się nie da.

Ma to poważną konsekwencję: **błąd w sterowniku wywraca cały system**, a nie
tylko jeden program. Niebieski ekran w Windowsie to najczęściej właśnie awaria
w trybie jądra.

!!! note "Nowsze podejście"

    Ponieważ sterowniki w jądrze są ryzykowne, współczesne systemy przenoszą ich
    część do trybu użytkownika. Windows ma do tego osobny mechanizm (UMDF) —
    działają tak np. sterowniki wielu urządzeń USB czy skanerów. Awaria takiego
    sterownika nie zabija systemu. Dla sprzętu wymagającego szybkiej reakcji,
    jak karty graficzne, tryb jądra pozostaje standardem.

---

## 3. System plików

:material-plus-circle: **rozszerzenie**

Dysk to w istocie ponumerowany zbiór bloków. **System plików** to sposób
zorganizowania tych bloków tak, by dało się mówić o „pliku" i „folderze":
przechowuje, w których blokach leży dany plik, jak się nazywa, kiedy powstał
i kto ma do niego dostęp.

To część systemu operacyjnego — dlatego Windows domyślnie nie odczyta dysku
sformatowanego w systemie plików Linuksa.

| System plików | Gdzie spotkasz | Warto wiedzieć |
| --- | --- | --- |
| **NTFS** | dyski systemowe Windows | uprawnienia, szyfrowanie, dziennik zmian |
| **exFAT** | duże pendrive'y, karty SD | czytany przez Windows, macOS i Linux |
| **FAT32** | stare pendrive'y, pamięci w sprzęcie | **plik maksymalnie 4 GB** |
| **ext4** | Linux | domyślny w większości dystrybucji |
| **APFS** | macOS | zoptymalizowany pod dyski SSD |

!!! warning "Skąd się bierze pytanie „dlaczego nie mogę skopiować tego filmu na pendrive'a?”"

    Pendrive jest sformatowany w FAT32, a plik ma więcej niż 4 GB. Miejsca jest
    dość, ale system plików nie potrafi zaadresować większego pliku. Rozwiązanie:
    sformatować nośnik w exFAT — pamiętając, że formatowanie **usuwa wszystkie
    dane**.

### :material-console: Ćwiczenie 1 — sprawdź system plików swojego dysku

=== "Sposób graficzny"

    1. Otwórz **Eksplorator plików** → **Ten komputer**.
    2. Kliknij prawym przyciskiem dysk `C:` → **Właściwości**.
    3. Odczytaj pole **System plików** na zakładce **Ogólne**.

=== "Wiersz poleceń"

    Otwórz **Wiersz polecenia** (`Win + R`, wpisz `cmd`) i wykonaj:

    ```bat
    fsutil fsinfo volumeinfo C:
    ```

    W odpowiedzi znajdź wiersz `File System Name`.

**Wynik zapisz w karcie pracy — zadanie 1.** Potrzebujesz litery dysku, systemu
plików, pojemności i wolnego miejsca, a do tego zrzutu ekranu. Jeśli w komputerze
jest więcej niż jeden dysk lub partycja, sprawdź każdą — bywa, że dysk systemowy
ma NTFS, a przenośny exFAT.

---

## 4. Fragmentacja i defragmentacja

:material-plus-circle: **rozszerzenie**

Gdy zapisujesz plik, system szuka wolnych bloków. Jeśli nie ma dość dużego
ciągłego obszaru, dzieli plik na kawałki i rozmieszcza je w różnych miejscach
dysku. To **fragmentacja**.

Na **dysku talerzowym (HDD)** ma to realne znaczenie: głowica musi fizycznie
przemieścić się nad każdy fragment, a każdy taki ruch to kilka milisekund.
Poskładanie plików w całość — **defragmentacja** — potrafi zauważalnie przyspieszyć
odczyt.

!!! danger "Dysku SSD się nie defragmentuje"

    W dysku SSD nie ma ruchomej głowicy — dostęp do każdej komórki trwa tyle
    samo, więc rozproszenie pliku nie spowalnia odczytu. Co gorsza,
    defragmentacja to ogromna liczba zapisów, a komórki pamięci SSD mają
    ograniczoną ich liczbę. **Ręczna defragmentacja SSD skraca jego życie, nie
    dając nic w zamian.**

    Windows o tym wie. Narzędzie nazywa się dziś **Optymalizuj dyski** i dla SSD
    wykonuje zupełnie inną operację — **TRIM**, czyli informuje dysk, które bloki
    są już nieużywane i można je wyczyścić. Zostaw to ustawienie domyślne.

### :material-console: Ćwiczenie 2 — oceń, czy twój dysk wymaga defragmentacji

1. Naciśnij `Win`, wpisz **Defragmentuj** i uruchom **Defragmentuj i optymalizuj
   dyski**.
2. Odczytaj kolumnę **Typ nośnika** — to ona mówi, czy masz SSD, czy HDD.
3. Zaznacz dysk i kliknij **Analizuj**. *(Dla SSD przycisk bywa nieaktywny — to
   prawidłowe zachowanie.)*
4. Odczytaj procent fragmentacji.

Możesz też sprawdzić to poleceniem — uruchom wiersz poleceń **jako administrator**:

```bat
defrag C: /A
```

Przełącznik `/A` oznacza *analizuj*: polecenie tylko raportuje stan i niczego nie
zmienia.

**Wynik i wniosek zapisz w karcie pracy — zadanie 2.** Wniosek sformułuj według
wzoru: *dysk C: jest typu … , poziom fragmentacji wynosi … %, defragmentacja jest
/ nie jest zalecana, ponieważ … .* Uzasadnienie ma odwoływać się do budowy
nośnika, a nie do samego procentu.

!!! tip "Kiedy defragmentacja HDD ma sens"

    Praktyczny próg to około **10%** fragmentacji. Poniżej zysk jest niezauważalny.

---

## 5. Konta użytkowników i uprawnienia

Komputer w pracowni używany jest przez kilkanaście osób. Bez osobnych kont każdy
widziałby pliki każdego, a jedna nieostrożna instalacja psułaby system wszystkim.

Konto użytkownika daje trzy rzeczy: **oddzielone dane** (własny pulpit
i dokumenty), **własne ustawienia** oraz **ograniczone uprawnienia**.

### Dwa typy kont w Windows

**Konto standardowe** — pozwala pracować, ale nie pozwala zmieniać ustawień
systemu ani instalować programów dla wszystkich użytkowników.

**Konto administratora** — może wszystko, łącznie z usunięciem systemu.

!!! tip "Zasada najmniejszych uprawnień"

    Na co dzień pracuj na koncie standardowym, nawet na własnym komputerze.
    Jeśli złośliwe oprogramowanie uruchomi się z twoimi uprawnieniami, a te są
    ograniczone — szkody też będą ograniczone. Okienko **Kontroli konta
    użytkownika (UAC)**, które pyta o zgodę na zmianę, nie jest utrudnieniem.
    Jest ostatnim momentem, w którym możesz powiedzieć „nie".

---

## 6. Hasła — co naprawdę działa

Wiele materiałów wciąż powtarza radę: „mieszaj wielkie i małe litery, cyfry
i znaki specjalne, zmieniaj hasło co miesiąc". **Amerykański instytut NIST, który
tę radę kiedyś sformułował, dziś jej nie zaleca.** Powód jest prosty: ludzie
reagują na wymuszoną złożoność przewidywalnie. `Haslo1!` staje się `Haslo2!`,
a potem `Haslo3!`.

### Aktualne zalecenia

**Długość ma większe znaczenie niż złożoność.** Cztery przypadkowe słowa są
trudniejsze do złamania i łatwiejsze do zapamiętania niż osiem poprzekręcanych
znaków.

**Nie zmieniaj hasła okresowo bez powodu.** Hasło zmienia się wtedy, gdy istnieje
podejrzenie, że wyciekło.

**Nie używaj haseł, które już wyciekły.** Bazy wykradzionych haseł są publicznie
dostępne i to od nich zaczyna każdy atakujący.

**Każde konto ma własne hasło.** Jeden wyciek nie może otwierać wszystkich drzwi.

**Używaj menedżera haseł.** Nie da się zapamiętać czterdziestu różnych haseł —
i nie trzeba.

**Włącz uwierzytelnianie dwuskładnikowe (2FA)** wszędzie, gdzie jest dostępne.
Nawet skradzione hasło nie wystarczy wtedy do zalogowania.

!!! example "Które hasło jest mocniejsze?"

    ```text
    P@ssw0rd!        (9 znaków, „złożone”)
    poziomka-wiatrak-27-beczka   (26 znaków, same małe litery i cyfry)
    ```

    Pierwsze znajduje się na każdej liście popularnych haseł i padnie w ułamku
    sekundy. Drugie jest dłuższe, nieprzewidywalne i łatwiejsze do zapamiętania.

---

## 7. Konto w środowisku aplikacji Google

Konto Google jest przykładem **konta w usłudze sieciowej**: dane i ustawienia
leżą na serwerze dostawcy, a ty dostajesz się do nich z dowolnego urządzenia.
To wygodne i jednocześnie warte zrozumienia — bo dane przestają być wyłącznie
twoje.

### :material-console: Ćwiczenie 3 — cykl życia konta

**Założenie konta**

1. Wejdź na `accounts.google.com` i wybierz **Utwórz konto**.
2. Wypełnij dane i ustaw hasło zgodnie z zasadami z sekcji 6.
3. Włącz **weryfikację dwuetapową** w sekcji *Bezpieczeństwo*.

**Przegląd tego, co konto o tobie wie**

4. Otwórz **Moje konto → Dane i prywatność**.
5. Sprawdź, jaka aktywność jest zapisywana i wyłącz to, czego nie chcesz.
6. Zobacz listę **aplikacji z dostępem do konta** i usuń zbędne.

**Usunięcie konta**

7. **Dane i prywatność → Więcej opcji → Usuń konto Google**.
8. Zanim potwierdzisz, pobierz swoje dane przez **Google Takeout**.

!!! warning "Zanim usuniesz cokolwiek na lekcji"

    Ćwiczenie wykonuj na **koncie testowym założonym na tych zajęciach**, nigdy
    na koncie prywatnym. Usunięcie konta Google jest nieodwracalne po upływie
    okresu karencji, a razem z kontem znika poczta, dysk i wszystko, co było
    z nim powiązane.

    To ćwiczenie robimy wspólnie na lekcji i **nie wchodzi do karty pracy** —
    w karcie odpowiadasz tylko na pytania o konta i hasła.

---

## 8. Praca w środowisku sieciowym

W szkolnej pracowni komputery nie działają w oderwaniu od siebie. Twoje konto,
pliki i uprawnienia mogą być przechowywane na serwerze — dzięki temu logujesz się
na dowolnym stanowisku i zastajesz swoje środowisko.

**Konto lokalne** istnieje na jednym komputerze. **Konto sieciowe (domenowe)**
istnieje na serwerze i działa na każdym komputerze w sieci.

Z zasobów sieciowych korzystasz zwykle przez **udziały sieciowe** — foldery na
serwerze widoczne pod adresem w postaci `\\serwer\nazwa_udziału`. Taki folder
można **zamapować jako dysk**, żeby pojawił się w Eksploratorze pod własną literą.

```bat
:: podłączenie udziału jako dysk Z:
net use Z: \\serwer\materialy

:: sprawdzenie aktywnych połączeń
net use

:: odłączenie
net use Z: /delete
```

!!! note "Dlaczego to ważne przy pracy z plikami"

    Pliki na dysku sieciowym nie są na twoim komputerze. Jeśli sieć przestanie
    działać w połowie zapisu, plik może zostać uszkodzony. Przy dłuższej pracy
    kopiuj plik lokalnie, pracuj, a gotowy wynik odłóż na dysk sieciowy.

---

## 9. Instalacja i aktualizacja oprogramowania

### Skąd instalować

Kolejność zaufania jest zawsze taka sama: **oficjalny sklep systemu** (Microsoft
Store), potem **strona producenta programu**, a dopiero na końcu cokolwiek innego.
Serwisy zbierające instalatory z całego internetu bardzo często dokładają do nich
własne dodatki.

Windows ma też menedżer pakietów działający z wiersza poleceń:

```bat
:: wyszukanie programu
winget search vlc

:: instalacja
winget install VideoLAN.VLC

:: aktualizacja wszystkiego, co da się zaktualizować
winget upgrade --all
```

!!! danger "Czerwone flagi przy instalacji"

    - instalator proponuje „dodatkowe oprogramowanie" zaznaczone domyślnie
    - program płatny jest oferowany za darmo z „crackiem"
    - strona pobierania ma kilka przycisków **Pobierz**, a właściwy jest najmniejszy
    - plik `.exe` przyszedł mailem albo komunikatorem

### Po co aktualizacje

Aktualizacja to nie tylko nowe funkcje. Większość poprawek zamyka **luki
bezpieczeństwa** — a informacja o luce jest publiczna od dnia wydania łatki.
Niezaktualizowany system to system, którego słabe punkty każdy może sprawdzić
w internecie.

---

## 10. Kopia zapasowa

Dysk nie ostrzega, że za chwilę przestanie działać. Pytanie nie brzmi, czy
stracisz kiedyś dane, tylko czy będziesz mieć wtedy kopię.

!!! abstract "Zasada 3-2-1"

    **3** kopie danych · na **2** różnych nośnikach · **1** poza budynkiem

    Trzecia część jest tą, o której najczęściej się zapomina. Kopia na drugim
    dysku w tym samym komputerze nie przetrwa kradzieży, zalania ani przepięcia.

### Co Windows oferuje

**Historia plików** — automatyczne kopie dokumentów na dysk zewnętrzny,
z możliwością cofnięcia się do wcześniejszej wersji pliku.

**Obraz systemu** — pełna kopia dysku systemowego wraz z programami
i ustawieniami. Odtworzenie przywraca komputer do stanu z dnia wykonania kopii.

**Kopia w chmurze** (OneDrive) — synchronizacja wybranych folderów. Uwaga: to
synchronizacja, nie kopia zapasowa. Plik usunięty na komputerze zniknie
i w chmurze, choć zwykle da się go odzyskać z kosza usługi przez pewien czas.

---

## 11. Gdy system się nie uruchamia

:material-star: **dopełnienie**

### Tryb awaryjny

Windows startuje wtedy z minimalnym zestawem sterowników i usług. Jeśli w trybie
awaryjnym działa, a normalnie nie — winowajcą jest coś, co w trybie awaryjnym się
nie ładuje: sterownik albo program uruchamiany przy starcie.

**Jak wejść:** przytrzymaj `Shift` i kliknij **Uruchom ponownie**, następnie
**Rozwiąż problemy → Opcje zaawansowane → Ustawienia uruchamiania → Uruchom
ponownie** i wybierz numer opcji.

| Opcja | Kiedy jej użyć |
| --- | --- |
| Tryb awaryjny | podstawowa diagnostyka, odinstalowanie sterownika |
| Tryb awaryjny z obsługą sieci | gdy potrzebujesz internetu, np. by pobrać sterownik |
| Tryb awaryjny z wierszem polecenia | gdy pulpit w ogóle się nie ładuje |
| Wyłącz wymuszanie podpisów sterowników | instalacja sterownika bez podpisu cyfrowego |
| Wyłącz automatyczne ponowne uruchamianie | żeby zdążyć przeczytać treść błędu |

### Nośnik awaryjny

To pendrive, z którego komputer wystartuje, gdy system na dysku jest uszkodzony.
Pozwala odzyskać pliki albo naprawić rozruch.

**Jak przygotować:** pobierz ze strony Microsoftu **Media Creation Tool**,
uruchom, wybierz *Utwórz nośnik instalacyjny*, wskaż pendrive'a (min. 8 GB).
Przy starcie komputera wejdź do menu rozruchu (najczęściej `F12`) i wskaż
pendrive'a. Zamiast instalować, wybierz **Napraw komputer**.

!!! tip "Zrób to zawczasu"

    Nośnik awaryjny przygotowuje się wtedy, gdy komputer jeszcze działa.
    Po awarii jest już za późno.

---

## 12. Wiersz poleceń

:material-star: **dopełnienie**

Nie wszystko da się zrobić klikaniem, a część rzeczy da się zrobić szybciej
pisaniem. Uruchom **Wiersz polecenia** (`Win + R` → `cmd`) — część poleceń wymaga
uprawnień administratora.

```bat
:: informacje o systemie: wersja, model, RAM, czas pracy
systeminfo

:: konfiguracja sieci
ipconfig /all

:: lista działających procesów
tasklist

:: sprawdzenie integralności plików systemowych  [administrator]
sfc /scannow

:: sprawdzenie dysku pod kątem błędów  [administrator]
chkdsk C:

:: analiza fragmentacji  [administrator]
defrag C: /A

:: informacje o systemie plików
fsutil fsinfo volumeinfo C:
```

!!! note "PowerShell"

    W nowszych wersjach Windows domyślną powłoką jest **PowerShell**, który
    obsługuje wszystkie powyższe polecenia, a dodatkowo pozwala pisać skrypty.
    Na razie wystarczy ci wiedza, że istnieje.

---

## Praca do oddania

Z tego tematu oddajesz **kartę pracy** — wypełniasz ją na komputerze, nie
w zeszycie.

[:material-file-word: Pobierz kartę pracy (.docx)](../pliki/karta-pracy-systemy-operacyjne.docx){ .md-button .md-button--primary download }

Karta zbiera to, co robiłeś przy komputerze w ćwiczeniach 1 i 2, plus pytania
o polecenia tekstowe, konta i hasła. Na końcu jest jedno zadanie do wyboru na
ocenę wyższą.

### Jak ją wypełnić

1. Otwórz plik w programie Word (albo w Wordzie w przeglądarce, albo
   w LibreOffice Writer — kartę da się wypełnić w każdym z nich).
2. Odpowiedzi wpisuj w jasne pola. Rozciągają się same, gdy tekstu jest więcej.
3. Zrzut ekranu robisz skrótem ++win+shift+s++, zaznaczasz fragment, a potem
   wklejasz w wyznaczoną ramkę skrótem ++ctrl+v++.
4. Zapisz plik pod nazwą `1TT_NrWDzienniku_SO.docx` — na przykład
   `1TT_12_SO.docx`.

### Jak ją oddać

Wchodzisz w **Dziennik VULCAN → Zadania domowe**, otwierasz zadanie *Systemy
operacyjne — karta pracy* i dołączasz plik jako załącznik. Jeśli w twoim widoku
załączniki są niedostępne, wklej odpowiedzi w pole tekstowe, a zrzuty ekranu
opisz słowami — wtedy zamiast obrazka podaj odczytane wartości.

!!! warning "Zanim wyślesz — zasłoń to, czego nie chcesz oddawać"

    Zrzuty z poleceń `systeminfo` i `ipconfig` potrafią pokazać numer seryjny,
    identyfikator produktu i nazwę komputera. Zamaluj je przed wklejeniem.
    To temat o bezpieczeństwie, więc zacznij od siebie — a przy okazji masz
    gotową odpowiedź na pytanie z zadania 3.

---

## Zadania sprawdzające

To pytania do samodzielnego sprawdzenia się przed sprawdzianem — **nie oddajesz
ich**, odpowiedzi masz od razu pod spodem. Pracę do oddania opisano wyżej.

??? question "1. Wymień pięć zadań systemu operacyjnego."

    Zarządzanie procesami, zarządzanie pamięcią, zarządzanie urządzeniami
    (sterowniki), zarządzanie plikami, udostępnianie interfejsu użytkownika.

??? question "2. W jakim trybie pracuje sterownik urządzenia i jaka jest tego konsekwencja?"

    W większości systemów operacyjnych — w **trybie jądra**, ponieważ musi mieć
    bezpośredni dostęp do sprzętu i obsługiwać przerwania. Konsekwencja: błąd
    w sterowniku powoduje awarię całego systemu, a nie pojedynczego programu.

??? question "3. Kolega nie może skopiować pliku 6 GB na pendrive'a, na którym jest 50 GB wolnego miejsca. Co się dzieje i co doradzisz?"

    Pendrive jest sformatowany w **FAT32**, który nie obsługuje plików większych
    niż 4 GB. Rozwiązanie: przenieść dane z pendrive'a, sformatować go w **exFAT**
    i skopiować plik ponownie. Alternatywnie — podzielić plik archiwizatorem na
    mniejsze części.

??? question "4. Czy warto defragmentować dysk SSD? Uzasadnij."

    Nie. W SSD nie ma ruchomej głowicy, więc fragmentacja nie wpływa na czas
    dostępu, a defragmentacja generuje ogromną liczbę zapisów i skraca żywotność
    komórek pamięci. Windows dla SSD wykonuje zamiast tego **TRIM**.

??? question "5. Dlaczego wymuszanie zmiany hasła co 30 dni pogarsza bezpieczeństwo?"

    Bo użytkownicy zmieniają hasła przewidywalnie — dopisując kolejną cyfrę albo
    znak. Powstają hasła słabsze i częściej zapisywane w widocznym miejscu.
    Aktualne zalecenia mówią, by zmieniać hasło tylko przy podejrzeniu wycieku,
    a stawiać na długość i menedżer haseł.

??? question "6. Wyjaśnij zasadę 3-2-1 i powiedz, czego brakuje w kopii trzymanej na drugim dysku w tym samym komputerze."

    Trzy kopie danych, na dwóch różnych nośnikach, jedna poza budynkiem. Kopia na
    drugim dysku w tej samej obudowie spełnia warunek dwóch nośników, ale nie
    chroni przed kradzieżą, pożarem, zalaniem ani przepięciem — brakuje kopii
    poza lokalizacją.

??? question "7. Komputer uruchamia się w trybie awaryjnym, ale normalnie pokazuje niebieski ekran. O czym to świadczy i od czego zaczniesz?"

    Problem leży w czymś, co ładuje się przy normalnym starcie, a w trybie
    awaryjnym nie: najczęściej w sterowniku lub programie autostartu. Zaczynam od
    przypomnienia sobie, co ostatnio instalowałem, i odinstalowuję to w trybie
    awaryjnym; sprawdzam też datę ostatniej aktualizacji sterowników.

??? question "8. Jakim poleceniem sprawdzisz poziom fragmentacji dysku C:, nie zmieniając niczego?"

    `defrag C: /A` — przełącznik `/A` oznacza wyłącznie analizę. Polecenie
    wymaga uprawnień administratora.

---

## Na ocenę celującą

Zadania wykraczające poza program. Wybierz jedno i przygotuj krótkie omówienie.

1. **Porównaj systemy plików NTFS i ext4** pod kątem sposobu zapisu metadanych
   i mechanizmu księgowania (*journaling*). Który i dlaczego lepiej znosi nagłą
   utratę zasilania?

2. **Zbadaj czas rozruchu swojego komputera.** Użyj `systeminfo` oraz Menedżera
   zadań (zakładka *Uruchamianie*), zidentyfikuj programy najbardziej opóźniające
   start i zmierz różnicę po ich wyłączeniu. Przedstaw wynik jako pomiar
   z liczbami, nie jako wrażenie.

3. **Uruchom dowolną dystrybucję Linuksa z pendrive'a** w trybie *live* i porównaj
   z Windowsem: sposób zarządzania kontami, instalacji oprogramowania i strukturę
   katalogów. Czym różni się `/home` od `C:\Users`?

4. **Napisz skrypt w PowerShellu**, który zbiera informacje o systemie (wersja,
   RAM, dyski, system plików każdego wolumenu) i zapisuje je do pliku tekstowego
   opatrzonego datą.

---

!!! info "Źródła i materiały uzupełniające"

    - Aktualne zalecenia dotyczące haseł: [NIST SP 800-63 — FAQ](https://pages.nist.gov/800-63-FAQ/)
    - Dokumentacja poleceń Windows: [Windows Commands](https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands)
    - Podręcznik: *Informatyka na czasie* — zakres rozszerzony, część 1, rozdział 1
