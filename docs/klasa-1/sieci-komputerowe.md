# Sieci komputerowe – budowa i usługi

!!! abstract "O tym temacie"

    **2 godziny lekcyjne** · Dział I. Urządzenia komputerowe w sieci
    · podstawa programowa **III.1**, **III.4**

    Sieć działa albo nie działa — i w drugim przypadku zaczyna się zgadywanie.
    Ta lekcja ma zamienić zgadywanie w procedurę: wiesz, jakie urządzenia są po
    drodze, jaki adres ma twój komputer, dokąd wysyła pakiety, gdy nie zna drogi,
    i którym poleceniem sprawdzisz, na którym odcinku połączenie się urywa.

!!! success "Cele lekcji"

    Po tych zajęciach potrafisz:

    1. wyjaśnić pojęcia: sieć komputerowa, protokół, adres IP, adres MAC
    2. rozróżnić sieci ze względu na zasięg (PAN, LAN, MAN, WAN) i opisać budowę sieci lokalnej
    3. wskazać rolę karty sieciowej, przełącznika, routera, punktu dostępowego i modemu
    4. odczytać konfigurację IP swojego komputera i rozpoznać, czy adres jest prywatny, publiczny czy APIPA
    5. objaśnić rolę maski podsieci, bramy domyślnej, serwera DNS i usługi DHCP
    6. wskazać usługi sieciowe i przypisać im protokoły oraz porty
    7. skonfigurować podstawowe ustawienia sieci bezprzewodowej i ocenić ich bezpieczeństwo
    8. zdiagnozować brak łączności poleceniami `ipconfig`, `ping`, `tracert` i `nslookup` oraz zinterpretować wynik testu prędkości
    9. wyjaśnić działanie NAT i model warstwowy TCP/IP

## Jak czytać tę stronę

Materiał jest ułożony narastająco. Sekcje oznaczone etykietami odpowiadają
poziomom wymagań — jeśli celujesz w ocenę dobrą lub wyższą, nie pomijaj ich.

| Etykieta | Poziom |
| --- | --- |
| bez etykiety | wymagania konieczne i podstawowe (oceny 2–3) |
| :material-plus-circle: **rozszerzenie** | wymagania rozszerzające (ocena 4) |
| :material-star: **dopełnienie** | wymagania dopełniające (ocena 5) |

[:material-file-document-outline: Ściąga sieciowa na jedną stronę (.docx)](../pliki/sieci-sciaga-1tt.docx){ .md-button download="sieci-sciaga-1tt.docx" }

---

## 1. Czym jest sieć komputerowa

**Sieć komputerowa** to co najmniej dwa urządzenia połączone tak, by mogły
wymieniać dane i dzielić zasoby: pliki, drukarkę, dostęp do internetu, moc
obliczeniową.

Żeby wymiana miała sens, obie strony muszą używać tych samych reguł. **Protokół**
to właśnie taki zestaw reguł: co wysłać, w jakiej kolejności, jak potwierdzić
odbiór i co zrobić, gdy dane zaginą. Jak rozmowa przez radio — bez ustalonego
„odbiór" nikt nie wie, kiedy jego kolej.

Dane nie płyną jednym strumieniem. Są dzielone na **pakiety**, każdy z nagłówkiem
(nadawca, odbiorca) i zawartością. Pakiety mogą dotrzeć różnymi drogami
i w innej kolejności — składanie ich z powrotem to zadanie protokołu.

### Podział ze względu na zasięg

| Skrót | Nazwa | Zasięg | Przykład |
| --- | --- | --- | --- |
| **PAN** | sieć osobista | kilka metrów | słuchawki Bluetooth, smartwatch |
| **LAN** | sieć lokalna | budynek, pracownia | sieć szkolna, sieć domowa |
| **MAN** | sieć miejska | miasto | sieć uczelni lub urzędu w kilku budynkach |
| **WAN** | sieć rozległa | kraj, kontynent | sieć operatora, połączenia między oddziałami firmy |

**Internet** jest siecią sieci: zbiorem połączonych ze sobą sieci lokalnych
i rozległych, które porozumiewają się wspólnym zestawem protokołów TCP/IP.
Nie ma jednego właściciela ani jednego centralnego komputera.

---

## 2. Z czego zbudowana jest sieć lokalna

### Medium transmisyjne

| Medium | Typowa prędkość | Uwagi |
| --- | --- | --- |
| Skrętka **Cat 5e** | 1 Gb/s | najczęstsza w szkołach i domach; do 100 m |
| Skrętka **Cat 6 / 6a** | 1–10 Gb/s | 10 Gb/s na krótszych odcinkach (Cat 6) lub do 100 m (Cat 6a) |
| **Światłowód** | 10 Gb/s i więcej | duże odległości, odporny na zakłócenia elektromagnetyczne |
| **Radio (Wi-Fi)** | zależnie od standardu | wygoda kosztem stabilności i bezpieczeństwa |

Ograniczenie 100 m dla skrętki to nie kaprys normy — dłuższy odcinek psuje
wykrywanie kolizji i tłumi sygnał. Dalej stosuje się światłowód albo kolejne
urządzenie pośredniczące.

### Urządzenia

**Karta sieciowa (NIC)** — łączy komputer z medium. Ma zapisany fabrycznie
**adres MAC**: 48 bitów, zapisywany szesnastkowo, np. `A4-5E-60-C1-3B-7F`.
Adres MAC identyfikuje urządzenie **w obrębie sieci lokalnej**.

**Przełącznik (switch)** — łączy urządzenia w sieci lokalnej. Uczy się, który
adres MAC jest na którym porcie, i kieruje ramkę tylko tam, gdzie trzeba.

**Router** — łączy różne sieci i wybiera drogę dla pakietów. To on decyduje,
którędy dane z twojego komputera wyjdą w świat.

**Punkt dostępowy (AP)** — udostępnia sieć drogą radiową. W domowym „routerze
Wi-Fi" siedzą zwykle w jednej obudowie: router, przełącznik i punkt dostępowy.

**Modem** — zamienia sygnał operatora (kabel, światłowód, sieć komórkowa) na
sygnał zrozumiały dla sieci lokalnej.

!!! tip "MAC czy IP — czym się różnią"

    **MAC** jest jak numer seryjny urządzenia: przypisany na stałe, niezależny od
    miejsca. **IP** jest jak adres pocztowy: zależy od sieci, w której właśnie
    jesteś, i zmienia się, gdy przeniesiesz laptop do domu. Przełącznik pracuje
    na adresach MAC, router — na adresach IP.

---

## 3. Adresacja IP

**Adres IPv4** to 32 bity zapisywane jako cztery liczby od 0 do 255, np.
`192.168.1.15`. Adres składa się z dwóch części: **część sieciowa** mówi,
w jakiej sieci jesteś, **część hosta** — którym urządzeniem w tej sieci.
Granicę między nimi wyznacza **maska podsieci**.

```text
adres IP   192.168.1.15
maska      255.255.255.0     (zapis skrócony: /24)
           └──── sieć ────┘ └host┘

adres sieci          192.168.1.0
adres rozgłoszeniowy 192.168.1.255
adresy dla urządzeń  192.168.1.1 – 192.168.1.254   (254 hosty)
```

Z puli adresów zawsze wypadają dwa: **adres sieci** (same zera w części hosta)
i **adres rozgłoszeniowy** (same jedynki), którym wysyła się dane do wszystkich
urządzeń w sieci naraz.

### Adresy prywatne i publiczne

Adresy prywatne to trzy pule zarezerwowane do użytku w sieciach lokalnych. Nie
są routowane w internecie — każda sieć domowa może używać ich niezależnie.

| Pula | Zakres | Gdzie spotykana |
| --- | --- | --- |
| `10.0.0.0/8` | 10.0.0.0 – 10.255.255.255 | duże sieci firmowe |
| `172.16.0.0/12` | 172.16.0.0 – 172.31.255.255 | sieci firmowe, maszyny wirtualne |
| `192.168.0.0/16` | 192.168.0.0 – 192.168.255.255 | sieci domowe i szkolne |

Dwa adresy warto rozpoznawać od razu:

- `127.0.0.1` — **pętla zwrotna** (*localhost*); to zawsze ten komputer;
- `169.254.x.x` — **APIPA**: komputer nie dostał adresu z DHCP i nadał go sobie
  sam. Taki adres oznacza, że łączności z serwerem DHCP nie ma — i to jest
  pierwsza rzecz, jaką widać, gdy sieć „nie działa".

### Co jeszcze musi wiedzieć komputer

**Brama domyślna** (*default gateway*) — adres routera, do którego komputer
wysyła wszystko, czego nie potrafi dostarczyć sam, czyli ruch poza sieć lokalną.
Zwykle `192.168.x.1`.

**Serwer DNS** — zamienia nazwę `pceikz.pl` na adres IP. Bez działającego DNS
strony nie otworzysz po nazwie, choć `ping 1.1.1.1` będzie działał — to typowy
objaw pozwalający natychmiast zawęzić przyczynę awarii.

**DHCP** — usługa, która automatycznie przydziela urządzeniom adres IP, maskę,
bramę i serwery DNS. Adres jest **dzierżawiony** na określony czas i po jego
upływie odnawiany. Serwer DHCP działa najczęściej na routerze.

:material-star: **dopełnienie** — adresów IPv4 jest nieco ponad 4 miliardy
i dawno się skończyły. Doraźnym rozwiązaniem jest NAT (sekcja 6), docelowym —
**IPv6** ze 128-bitowym adresem, zapisywanym szesnastkowo, np.
`2001:0db8:85a3::8a2e:0370:7334`. Szczegółowo zajmiemy się nim na kolejnej lekcji.

---

## 4. Usługi sieciowe i porty

Adres IP wskazuje **komputer**, numer portu — **usługę** na tym komputerze.
Dlatego jeden serwer może jednocześnie obsługiwać stronę i pocztę.

| Usługa | Protokół | Port | Do czego |
| --- | --- | :---: | --- |
| Strony WWW | HTTP | 80 | transmisja nieszyfrowana |
| Strony WWW | HTTPS | 443 | transmisja szyfrowana TLS — standard |
| Nazwy domen | DNS | 53 | zamiana nazwy na adres IP |
| Automatyczna konfiguracja | DHCP | 67, 68 | przydzielanie adresów |
| Przesyłanie plików | FTP / SFTP | 21 / 22 | FTP przesyła hasło jawnym tekstem |
| Zdalny terminal | SSH | 22 | szyfrowana praca na zdalnym systemie |
| Poczta — wysyłanie | SMTP | 25, 587 | |
| Poczta — odbiór | IMAP | 143, 993 | 993 to wersja szyfrowana |
| Udostępnianie plików w LAN | SMB | 445 | dyski sieciowe, drukarki w Windows |

W sieci szkolnej korzystasz z nich, nawet o tym nie myśląc: dysk sieciowy to
SMB, drukarka w sekretariacie to usługa druku, dziennik VULCAN to HTTPS,
a logowanie na stanowisku może sprawdzać kontroler domeny.

!!! warning "HTTP kontra HTTPS"

    Kłódka w pasku adresu oznacza tylko tyle, że **transmisja jest szyfrowana** —
    nikt po drodze nie odczyta hasła. Nie znaczy, że strona jest uczciwa:
    certyfikat dla domeny wyłudzającej dane też można wystawić. Kłódka mówi
    „nikt nie podsłuchuje", nie „można ufać".

---

## 5. Sieć bezprzewodowa :material-plus-circle: **rozszerzenie**

### Pasma i standardy

Wi-Fi pracuje w pasmach **2,4 GHz** (większy zasięg, mniejsza prędkość, dużo
zakłóceń), **5 GHz** (szybciej, ale gorzej przez ściany) oraz **6 GHz**
(najnowsze, najmniej zatłoczone).

| Nazwa handlowa | Standard | Pasma | Uwagi |
| --- | --- | --- | --- |
| Wi-Fi 4 | 802.11n | 2,4 / 5 GHz | wciąż spotykany w starszym sprzęcie |
| Wi-Fi 5 | 802.11ac | 5 GHz | długo najpopularniejszy |
| Wi-Fi 6 / 6E | 802.11ax | 2,4 / 5 (/ 6) GHz | lepsza praca przy wielu urządzeniach |
| Wi-Fi 7 | 802.11be | 2,4 / 5 / 6 GHz | kanały do 320 MHz, modulacja 4096-QAM, praca w wielu pasmach naraz (MLO) |

Certyfikację Wi-Fi 7 uruchomiono 8 stycznia 2024 r., a sam standard 802.11be
opublikowano 22 lipca 2025 r. Kolejna generacja — Wi-Fi 8 (802.11bn) —
jest w opracowaniu i spodziewana około 2028 r.

### Zabezpieczenia

**WPA3** to obecny standard, **WPA2** — wciąż akceptowalne minimum. **WEP i WPA
(pierwszej wersji) są złamane** i nie zabezpieczają niczego.

!!! danger "Cztery rzeczy, które trzeba zrobić w nowym routerze"

    1. **Zmienić hasło administratora routera** — fabryczne bywa wypisane na
       naklejce i w instrukcji dostępnej w internecie.
    2. **Ustawić WPA3 lub WPA2 i własne, długie hasło Wi-Fi.**
    3. **Włączyć automatyczne aktualizacje oprogramowania układowego.**
    4. **Wyłączyć WPS** — przycisk „szybkiego parowania" bywa podatny na atak.

    Czego **nie** trzeba robić: ukrywać nazwy sieci (SSID). To nie jest
    zabezpieczenie — nazwa i tak jest widoczna w ruchu, a utrudnia tylko
    życie własnym użytkownikom. Filtrowanie adresów MAC też nie jest ochroną,
    bo adres MAC da się podmienić.

---

## 6. NAT i model warstwowy :material-star: **dopełnienie**

### NAT — jeden adres publiczny na cały dom

Operator przydziela zwykle **jeden publiczny adres IP**, a urządzeń w domu jest
kilkanaście. **NAT** (*Network Address Translation*) działa na routerze:
podmienia w wychodzących pakietach adres prywatny na publiczny i zapamiętuje
w tablicy, któremu urządzeniu odesłać odpowiedź — rozróżniając połączenia po
numerach portów.

```text
laptop  192.168.1.15:51000  ──►  router  ──►  83.24.11.7:40001  ──►  internet
telefon 192.168.1.22:49877  ──►  router  ──►  83.24.11.7:40002  ──►  internet
```

Skutek uboczny: połączenie z zewnątrz do konkretnego urządzenia w domu nie ma
jak trafić samo — trzeba je wskazać (przekierowanie portów). Dlatego serwer gry
czy kamera wymagają dodatkowej konfiguracji, a nie „po prostu działają".

### Model TCP/IP

| Warstwa | Co robi | Przykłady |
| --- | --- | --- |
| **Aplikacji** | rozmawia z użytkownikiem i programem | HTTP, DNS, SMTP, SSH |
| **Transportowa** | dzieli dane na segmenty, adresuje usługi portami | TCP (z potwierdzeniami), UDP (bez) |
| **Internetowa** | adresuje pakiety i wyznacza trasę | IP, ICMP (to nim działa `ping`) |
| **Dostępu do sieci** | wysyła bity medium | Ethernet, Wi-Fi |

Model **ISO/OSI** dzieli to samo drobniej, na siedem warstw — w praktyce mówi
się o nim przy opisie teoretycznym, a pracuje się na czterowarstwowym TCP/IP.

**TCP kontra UDP:** TCP potwierdza odbiór i retransmituje zgubione segmenty
(strony WWW, poczta, pliki). UDP nie potwierdza niczego, za to nie czeka —
dlatego używa się go tam, gdzie opóźnienie boli bardziej niż pojedyncza
zgubiona porcja danych: rozmowy głosowe, wideo na żywo, gry.

---

## 7. Diagnostyka w wierszu poleceń

Uruchom **Wiersz polecenia** (++win+r++ → `cmd`) i sprawdzaj **po kolei**, od
siebie na zewnątrz. Każdy krok odcina część możliwych przyczyn.

| Polecenie | Co pokazuje |
| --- | --- |
| `ipconfig /all` | adres IP, maskę, bramę, serwery DNS, adres MAC, serwer DHCP |
| `ping 127.0.0.1` | czy działa stos sieciowy tego komputera |
| `ping <brama>` | czy jest łączność z routerem |
| `ping 1.1.1.1` | czy jest łączność z internetem (po adresie, bez DNS) |
| `ping pceikz.pl` | czy działa rozwiązywanie nazw |
| `tracert pceikz.pl` | trasę pakietu, węzeł po węźle |
| `nslookup pceikz.pl` | jaki adres zwraca serwer DNS |
| `getmac` | adresy MAC kart sieciowych |
| `netstat -an` | otwarte połączenia i nasłuchujące porty |
| `ipconfig /release` + `/renew` | zwolnienie i pobranie nowej dzierżawy DHCP |
| `ipconfig /flushdns` | wyczyszczenie pamięci podręcznej DNS |

!!! tip "Czytanie wyniku, czyli gdzie leży usterka"

    | Co działa | Co nie działa | Wniosek |
    | --- | --- | --- |
    | brak adresu lub `169.254.x.x` | wszystko | nie ma odpowiedzi z DHCP — kabel, port, router |
    | ping do bramy | ping do `1.1.1.1` | problem poza siecią lokalną — u operatora albo na routerze |
    | ping do `1.1.1.1` | ping po nazwie | wina DNS — sprawdź adres serwera DNS, wyczyść pamięć podręczną |
    | ping po nazwie | strona w przeglądarce | sieć jest w porządku; przyczyna to serwer, przeglądarka albo filtr treści |

### :material-console: Ćwiczenie 1 — inwentaryzacja stanowiska

Wykonaj `ipconfig /all` i odczytaj: adres IPv4, maskę, bramę domyślną, serwery
DNS, adres fizyczny (MAC) i serwer DHCP. Ustal, czy twój adres jest prywatny
(z której puli?), publiczny czy APIPA. **Wynik zapisz w karcie pracy — zadanie 1.**

### :material-console: Ćwiczenie 2 — gdzie urywa się połączenie

Wykonaj po kolei: `ping 127.0.0.1`, `ping` do swojej bramy, `ping 1.1.1.1`,
`ping pceikz.pl`, a na koniec `tracert pceikz.pl` i `nslookup pceikz.pl`.
Zapisz czasy odpowiedzi i liczbę przeskoków w `tracert`.

Część węzłów w trasie odpowiada gwiazdkami — to nie awaria, tylko urządzenie
skonfigurowane tak, by nie odpowiadać na takie zapytania. **Wynik — zadanie 2.**

### :material-console: Ćwiczenie 3 — test prędkości i jego interpretacja

Wykonaj test prędkości łącza i odczytaj cztery wartości: **pobieranie**,
**wysyłanie**, **ping (opóźnienie)** i **jitter**.

!!! warning "Megabity to nie megabajty"

    Łącza sprzedaje się w **megabitach na sekundę (Mb/s)**, a pliki pobierają
    się w **megabajtach na sekundę (MB/s)**. Osiem bitów to jeden bajt, więc
    łącze 300 Mb/s daje w najlepszym razie około **37,5 MB/s**. To nie jest
    oszustwo operatora, tylko dwie różne jednostki — i typowe pytanie na
    sprawdzianie.

Przy grach i rozmowach ważniejsze od przepustowości bywa **opóźnienie**:
200 Mb/s z pingiem 120 ms gra się gorzej niż 50 Mb/s z pingiem 15 ms.
**Wynik i wnioski — zadanie 3.**

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Komputer po uruchomieniu ma adres 169.254.13.7. Co to oznacza?",
    "typ": "jedna",
    "opcje": [
      "Ma poprawny adres publiczny",
      "Nie otrzymał adresu z serwera DHCP i nadał go sobie sam (APIPA)",
      "Jest podłączony do sieci gościnnej",
      "Jego karta sieciowa jest uszkodzona"
    ],
    "poprawna": 1,
    "wyjasnienie": "Pula 169.254.x.x to APIPA. Sprawdzasz wtedy kabel, port przełącznika i to, czy serwer DHCP na routerze w ogóle działa."
  },
  {
    "pytanie": "Ping do 1.1.1.1 działa, ping do pceikz.pl zwraca błąd. Gdzie jest problem?",
    "typ": "jedna",
    "opcje": [
      "W karcie sieciowej komputera",
      "W rozwiązywaniu nazw — czyli w DNS",
      "W bramie domyślnej",
      "U operatora — nie ma połączenia z internetem"
    ],
    "poprawna": 1,
    "wyjasnienie": "Skoro pakiety docierają pod adres IP, warstwa niższa działa. Zawodzi zamiana nazwy na adres: sprawdź serwer DNS i wykonaj ipconfig /flushdns."
  },
  {
    "pytanie": "Adres 192.168.1.15 z maską 255.255.255.0 — ile urządzeń można zaadresować w tej sieci?",
    "typ": "jedna",
    "opcje": ["256", "254", "255", "512"],
    "poprawna": 1,
    "wyjasnienie": "Maska /24 zostawia 8 bitów na hosty, czyli 256 kombinacji. Odpadają dwie: adres sieci (192.168.1.0) i rozgłoszeniowy (192.168.1.255). Zostaje 254."
  },
  {
    "pytanie": "Czym różni się przełącznik (switch) od routera?",
    "typ": "jedna",
    "opcje": [
      "Przełącznik działa bezprzewodowo, a router po kablu",
      "Przełącznik łączy urządzenia w jednej sieci lokalnej i kieruje ramki po adresach MAC, a router łączy różne sieci i kieruje pakiety po adresach IP",
      "Router jest szybszy, bo ma więcej portów",
      "Przełącznik przydziela adresy IP, a router tylko przesyła dane"
    ],
    "poprawna": 1,
    "wyjasnienie": "W domowym urządzeniu oba są w jednej obudowie razem z punktem dostępowym, dlatego łatwo je pomylić."
  },
  {
    "pytanie": "Do czego służy brama domyślna?",
    "typ": "jedna",
    "opcje": [
      "Do szyfrowania ruchu wychodzącego",
      "To adres urządzenia, do którego komputer wysyła ruch kierowany poza własną sieć lokalną",
      "Do zamiany nazw domen na adresy IP",
      "Do przydzielania adresów IP w sieci lokalnej"
    ],
    "poprawna": 1,
    "wyjasnienie": "Jeśli adres docelowy nie należy do sieci lokalnej, pakiet idzie do bramy — czyli zwykle do routera."
  },
  {
    "pytanie": "Łącze ma 300 Mb/s. Jaka jest maksymalna realna prędkość pobierania pliku w MB/s?",
    "typ": "jedna",
    "opcje": ["300 MB/s", "około 37,5 MB/s", "około 150 MB/s", "około 3 MB/s"],
    "poprawna": 1,
    "wyjasnienie": "Bity dzieli się przez osiem: 300 / 8 = 37,5 MB/s, i to w warunkach idealnych. Operator podaje megabity, menedżer pobierania — megabajty."
  },
  {
    "pytanie": "Po co routerowi mechanizm NAT?",
    "typ": "jedna",
    "opcje": [
      "Szyfruje ruch w sieci lokalnej",
      "Pozwala wielu urządzeniom z adresami prywatnymi korzystać z jednego adresu publicznego",
      "Przyspiesza transmisję przez kompresję pakietów",
      "Blokuje strony o niepożądanej treści"
    ],
    "poprawna": 1,
    "wyjasnienie": "Router podmienia adres źródłowy i zapamiętuje w tablicy, komu odesłać odpowiedź — rozróżnia połączenia po portach. Efekt uboczny: ruch przychodzący z zewnątrz wymaga przekierowania portu."
  },
  {
    "pytanie": "Którego zabezpieczenia sieci bezprzewodowej nie wolno dziś używać?",
    "typ": "jedna",
    "opcje": ["WPA3", "WPA2 z długim hasłem", "WEP", "WPA2 Enterprise"],
    "poprawna": 2,
    "wyjasnienie": "WEP został złamany dawno temu i daje wyłącznie złudzenie ochrony. Minimum to WPA2, standardem jest WPA3."
  },
  {
    "pytanie": "Która usługa i port odpowiadają za szyfrowane strony internetowe?",
    "typ": "jedna",
    "opcje": ["HTTP, port 80", "HTTPS, port 443", "DNS, port 53", "SMB, port 445"],
    "poprawna": 1,
    "wyjasnienie": "HTTPS na porcie 443. Kłódka oznacza jednak tylko szyfrowanie transmisji, a nie wiarygodność właściciela strony."
  },
  {
    "pytanie": "Rozmowa głosowa i transmisja wideo na żywo korzystają zwykle z UDP, a nie z TCP. Dlaczego?",
    "typ": "jedna",
    "opcje": [
      "UDP szyfruje dane, a TCP nie",
      "UDP nie czeka na potwierdzenia i retransmisje, więc opóźnienie jest mniejsze — a pojedyncza zgubiona porcja przeszkadza mniej niż zacinanie",
      "UDP przesyła więcej danych w jednym pakiecie",
      "TCP nie działa w sieciach bezprzewodowych"
    ],
    "poprawna": 1,
    "wyjasnienie": "W rozmowie liczy się czas. Powtórzona po sekundzie sylaba jest bezużyteczna, więc lepiej ją stracić niż opóźnić całą transmisję."
  }
]
</script>
</div>

---

## Karta pracy

Wypełnij kartę na tej stronie, a potem pobierz gotowy dokument Worda i oddaj go
przez **Zadania domowe w dzienniku VULCAN**.

<div class="karta-pracy" data-karta="sieci-komputerowe"></div>

---

## Sprawdź, czy rozumiesz

??? question "Dlaczego adres MAC nie wystarcza do przesłania danych przez internet?"

    Adres MAC działa wyłącznie w obrębie jednej sieci lokalnej i nie zawiera
    informacji o tym, gdzie ta sieć się znajduje. Routery wyznaczają trasę na
    podstawie adresów IP, w których część sieciowa mówi, do jakiej sieci należy
    odbiorca. MAC jest numerem urządzenia, IP — jego adresem w konkretnej sieci.

??? question "Uczeń ustawił w routerze ukrywanie nazwy sieci i filtrowanie adresów MAC, ale zostawił szyfrowanie WEP. Oceń poziom zabezpieczenia."

    Zabezpieczenie jest pozorne. Ukryty SSID i tak jest widoczny w ruchu
    radiowym, a adres MAC da się podmienić w kilka chwil. Jedynym realnym
    zabezpieczeniem byłoby szyfrowanie — a WEP jest złamany. Właściwa kolejność
    działań: WPA3 lub WPA2 z długim hasłem, zmiana hasła administratora routera,
    aktualizacje oprogramowania układowego.

??? question "`tracert` pokazuje w trzecim wierszu trzy gwiazdki, a mimo to trasa biegnie dalej i strona się otwiera. Co się stało?"

    Ten węzeł nie odpowiada na zapytania diagnostyczne — administrator tak go
    skonfigurował, zwykle ze względów bezpieczeństwa. Pakiety przechodzą przez
    niego normalnie. Gwiazdki oznaczają awarię tylko wtedy, gdy od tego miejsca
    trasa się urywa i nic dalej nie odpowiada.

??? question "W pracowni jest 28 komputerów, drukarka sieciowa i dwa punkty dostępowe. Czy maska /24 wystarczy? Uzasadnij liczbowo."

    Tak. Maska /24 daje 254 adresy dla urządzeń, a potrzeba ich 31 plus router.
    Zapas jest duży, co ma znaczenie przy urządzeniach gości i sprzęcie
    podłączanym doraźnie. Sieć o masce /27 (30 adresów) byłaby wypełniona
    niemal w całości i nie zostawiałaby miejsca na rozbudowę.

---

## Na ocenę celującą

Wybierz jedno zadanie i przygotuj dokumentację wyników.

1. **Projekt sieci dla pracowni z podziałem na podsieci.** Zaprojektuj adresację
   dla trzech grup: stanowiska uczniowskie (30 urządzeń), sprzęt nauczyciela
   i drukarki (8 urządzeń), sieć dla gości (20 urządzeń). Dla każdej podaj adres
   sieci, maskę, zakres adresów dla urządzeń i adres rozgłoszeniowy oraz uzasadnij
   dobór masek.

2. **Zmierz sieć, w której pracujesz.** Wykonaj serię testów prędkości i pingu
   o różnych porach dnia (minimum trzy pomiary), zestaw wyniki w tabeli i opisz,
   co się zmienia i dlaczego. Wynik ma być pomiarem z liczbami, nie wrażeniem.

3. **`tracert` do trzech kontynentów.** Prześledź trasę do serwera w Polsce,
   w Stanach Zjednoczonych i w Azji. Porównaj liczbę przeskoków i opóźnienia,
   a potem oszacuj, ile z tego czasu wynika z samej odległości — przyjmij, że
   sygnał w światłowodzie pokonuje około 200 000 km/s.

4. **Zadanie maturalne o podsieciach.** Znajdź w arkuszach maturalnych
   z informatyki zadanie dotyczące adresacji IP, rozwiąż je i zapisz tok
   rozumowania krok po kroku.

---

!!! info "Źródła i materiały uzupełniające"

    - Adresy prywatne: [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
    - Standardy Wi-Fi i certyfikacja: [Wi-Fi Alliance](https://www.wi-fi.org/)
    - Polecenia diagnostyczne Windows: [Windows Commands](https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands)
    - Podręcznik: *Informatyka na czasie* — zakres rozszerzony, część 1, dział I

*Dane o standardach sieci bezprzewodowych sprawdzone 12 września 2026 r.:
certyfikacja Wi-Fi 7 ruszyła 8 stycznia 2024 r., standard 802.11be opublikowano
22 lipca 2025 r., Wi-Fi 8 (802.11bn) jest spodziewane około 2028 r.*
