/* Wizualizator przeszukiwania labiryntu — DFS z nawrotami i BFS z kolejką.
 *
 * Autorowanie w Markdownie — kontener z danymi w znaczniku script:
 *
 *     <div class="labirynt" markdown="0">
 *     <script type="application/json">
 *     {
 *       "siatka": [
 *         "#########",
 *         "#S..#...#",
 *         "###.#.#.#",
 *         "#...#.#E#",
 *         "#########"
 *       ],
 *       "tryb": "dfs"
 *     }
 *     </script>
 *     </div>
 *
 * Znaki siatki: `#` ściana, `.` korytarz, `S` start, `E` wyjście.
 * Pole „tryb" (opcjonalne) ustawia algorytm startowy: "dfs" albo "bfs".
 *
 * Widget nic nie wysyła i niczego nie zapisuje — liczy w przeglądarce.
 * Oba algorytmy chodzą po tej samej siatce i w tej samej kolejności
 * sąsiadów (góra → prawo → dół → lewo), żeby różnica, którą widać na
 * ekranie, brała się wyłącznie ze struktury danych: stosu albo kolejki.
 */
(function () {
  "use strict";

  // Kolejność sprawdzania sąsiadów. Ta sama dla obu algorytmów — inaczej
  // porównanie nie byłoby uczciwe.
  // Nazwy w formie, która wchodzi prosto do zdania „idziemy …” —
  // nie w mianowniku, bo „idziemy w góra” to nie po polsku.
  const KIERUNKI = [
    { dr: -1, dc: 0, nazwa: "w górę" },
    { dr: 0, dc: 1, nazwa: "w prawo" },
    { dr: 1, dc: 0, nazwa: "w dół" },
    { dr: 0, dc: -1, nazwa: "w lewo" },
  ];

  const klucz = (r, c) => r + "," + c;

  /* Polska odmiana liczebnika: 1 krok, 2–4 kroki, 5+ kroków — z wyjątkiem
     nastek (12, 13, 14), które biorą formę dopełniaczową. Bez tego liczniki
     wypisywały „22 kroków" i „1 nowych sąsiadów". */
  function odmien(n, poj, mn, dop) {
    if (n === 1) return poj;
    const j = n % 10, d = n % 100;
    return (j >= 2 && j <= 4 && !(d >= 12 && d <= 14)) ? mn : dop;
  }

  const POLA = (n) => odmien(n, "pole", "pola", "pól");

  /* ───────────────────────────────────────────── odczyt siatki */
  function wczytaj(siatka) {
    const wiersze = siatka.map((w) => w.split(""));
    const szer = Math.max(...wiersze.map((w) => w.length));
    wiersze.forEach((w) => { while (w.length < szer) w.push("#"); });

    let start = null, wyjscie = null;
    wiersze.forEach((w, r) => w.forEach((z, c) => {
      if (z === "S") start = { r, c };
      if (z === "E") wyjscie = { r, c };
    }));
    if (!start || !wyjscie) throw new Error("siatka musi zawierać S i E");
    return { wiersze, wys: wiersze.length, szer, start, wyjscie };
  }

  const wolne = (lab, r, c) =>
    r >= 0 && r < lab.wys && c >= 0 && c < lab.szer && lab.wiersze[r][c] !== "#";

  /* ─────────────────────────────────────── stan przeszukiwania
     Jeden obiekt na jeden przebieg. Metoda krok() wykonuje dokładnie
     tyle pracy, ile na lekcji opisujemy jako „jeden krok algorytmu”,
     i zwraca zdanie do wypisania pod siatką. */
  function nowyStan(lab, tryb) {
    const s = {
      tryb,
      odwiedzone: new Set([klucz(lab.start.r, lab.start.c)]),
      pojemnik: [lab.start],          // stos (DFS) albo kolejka (BFS)
      skad: new Map(),                // tylko BFS: skąd przyszliśmy do pola
      biezaca: lab.start,
      sciezka: null,                  // wypełniana po znalezieniu wyjścia
      koniec: false,
      sukces: false,
      kroki: 0,
      opis: tryb === "dfs"
        ? "Start na stosie. Idziemy w głąb, dopóki się da."
        : "Start w kolejce. Rozchodzimy się falą, po jednym polu na krok.",
    };
    return s;
  }

  function sasiedzi(lab, pole) {
    return KIERUNKI
      .map((k) => ({ r: pole.r + k.dr, c: pole.c + k.dc, nazwa: k.nazwa }))
      .filter((p) => wolne(lab, p.r, p.c));
  }

  function krokDFS(lab, s) {
    if (!s.pojemnik.length) {
      s.koniec = true;
      s.opis = "Stos pusty — cofnęliśmy się aż do startu. Wyjścia nie ma.";
      return;
    }
    const biezaca = s.pojemnik[s.pojemnik.length - 1];   // wierzch stosu
    s.biezaca = biezaca;

    if (biezaca.r === lab.wyjscie.r && biezaca.c === lab.wyjscie.c) {
      // Przy DFS z nawrotami stos JEST bieżącą ścieżką — nic nie trzeba odtwarzać.
      s.sciezka = s.pojemnik.slice();
      s.koniec = true;
      s.sukces = true;
      s.opis = `Wyjście! Na stosie leży gotowa droga — ${s.sciezka.length} ${POLA(s.sciezka.length)}. `
             + "Nie musi być najkrótsza: to po prostu pierwsza, którą znaleźliśmy.";
      return;
    }

    const nowy = sasiedzi(lab, biezaca)
      .find((p) => !s.odwiedzone.has(klucz(p.r, p.c)));

    if (nowy) {
      s.odwiedzone.add(klucz(nowy.r, nowy.c));
      s.pojemnik.push(nowy);
      s.opis = `Z wierzchu stosu idziemy ${nowy.nazwa}. Nowe pole ląduje na stosie.`;
    } else {
      s.pojemnik.pop();
      s.opis = "Ślepy zaułek — wszystkie strony odwiedzone. **Nawrót**: zdejmujemy pole ze stosu.";
    }
    s.kroki += 1;
  }

  function krokBFS(lab, s) {
    if (!s.pojemnik.length) {
      s.koniec = true;
      s.opis = "Kolejka pusta — fala obeszła wszystko, co osiągalne. Wyjścia nie ma.";
      return;
    }
    const biezaca = s.pojemnik.shift();                  // początek kolejki
    s.biezaca = biezaca;

    if (biezaca.r === lab.wyjscie.r && biezaca.c === lab.wyjscie.c) {
      // Kolejka nie pamięta drogi — trzeba ją odtworzyć wstecz po mapie „skąd”.
      const droga = [];
      let p = biezaca;
      while (p) {
        droga.push(p);
        p = s.skad.get(klucz(p.r, p.c));
      }
      s.sciezka = droga.reverse();
      s.koniec = true;
      s.sukces = true;
      s.opis = `Wyjście! Droga odtworzona wstecz po mapie „skąd” — ${s.sciezka.length} ${POLA(s.sciezka.length)}. `
             + "To jest droga **najkrótsza**: BFS dociera do każdego pola w minimalnej liczbie ruchów.";
      return;
    }

    const nowe = sasiedzi(lab, biezaca)
      .filter((p) => !s.odwiedzone.has(klucz(p.r, p.c)));
    nowe.forEach((p) => {
      s.odwiedzone.add(klucz(p.r, p.c));
      s.skad.set(klucz(p.r, p.c), biezaca);
      s.pojemnik.push(p);
    });
    const ILU = ["", "jednego nowego sąsiada", "dwóch nowych sąsiadów", "trzech nowych sąsiadów", "czterech nowych sąsiadów"];
    s.opis = nowe.length
      ? `Zdejmujemy pole z początku kolejki i dokładamy na koniec ${ILU[nowe.length]}.`
      : "Zdejmujemy pole z początku kolejki — nowych sąsiadów brak, kolejka się skraca.";
    s.kroki += 1;
  }

  const krok = (lab, s) => (s.tryb === "dfs" ? krokDFS : krokBFS)(lab, s);

  /* ─────────────────────────────────────────────────── rysowanie */
  function zbuduj(host, lab, tryb) {
    host.innerHTML = `
      <div class="lb">
        <div class="lb-sterowanie">
          <div class="lb-tryby" role="group" aria-label="Wybór algorytmu">
            <button type="button" class="lb-tryb" data-tryb="dfs">DFS — stos</button>
            <button type="button" class="lb-tryb" data-tryb="bfs">BFS — kolejka</button>
          </div>
          <div class="lb-przyciski">
            <button type="button" class="lb-krok">Krok</button>
            <button type="button" class="lb-graj">Do końca</button>
            <button type="button" class="lb-reset">Od nowa</button>
          </div>
        </div>
        <div class="lb-siatka" role="img" aria-label="Labirynt"></div>
        <p class="lb-opis"></p>
        <div class="lb-liczniki">
          <span class="lb-licznik"><b class="lb-kroki">0</b> <span class="lb-kroki-sl">kroków</span></span>
          <span class="lb-licznik"><b class="lb-odw">1</b> odwiedzone <span class="lb-odw-sl">pole</span></span>
          <span class="lb-licznik lb-dlugosc" hidden>droga: <b class="lb-dl">—</b> <span class="lb-dl-sl">pól</span></span>
        </div>
        <div class="lb-pojemnik">
          <span class="lb-etykieta"></span>
          <span class="lb-zawartosc"></span>
        </div>
        <p class="lb-legenda">
          <span class="lb-poz"><span class="lb-kl lb-kl-sciana"></span> ściana</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-start"></span> start</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-wyjscie"></span> wyjście</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-odw"></span> odwiedzone</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-czeka"></span> czeka w strukturze</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-biez"></span> bieżące</span>
          <span class="lb-poz"><span class="lb-kl lb-kl-droga"></span> znaleziona droga</span>
        </p>
      </div>`;

    const siatka = host.querySelector(".lb-siatka");
    siatka.style.setProperty("--lb-kolumny", lab.szer);
    const komorki = [];
    for (let r = 0; r < lab.wys; r++) {
      komorki[r] = [];
      for (let c = 0; c < lab.szer; c++) {
        const d = document.createElement("div");
        d.className = "lb-pole" + (lab.wiersze[r][c] === "#" ? " lb-sciana" : "");
        siatka.appendChild(d);
        komorki[r][c] = d;
      }
    }
    return { komorki };
  }

  function odswiez(host, lab, s, widok) {
    const wStrukturze = new Set(s.pojemnik.map((p) => klucz(p.r, p.c)));
    const naDrodze = new Set((s.sciezka || []).map((p) => klucz(p.r, p.c)));

    for (let r = 0; r < lab.wys; r++) {
      for (let c = 0; c < lab.szer; c++) {
        const d = widok.komorki[r][c];
        if (lab.wiersze[r][c] === "#") continue;
        const k = klucz(r, c);
        d.className = "lb-pole";
        if (s.odwiedzone.has(k)) d.classList.add("lb-odwiedzone");
        if (wStrukturze.has(k)) d.classList.add("lb-czeka");
        if (naDrodze.has(k)) d.classList.add("lb-droga");
        if (!s.koniec && s.biezaca && s.biezaca.r === r && s.biezaca.c === c) {
          d.classList.add("lb-biezaca");
        }
        if (r === lab.start.r && c === lab.start.c) d.classList.add("lb-start");
        if (r === lab.wyjscie.r && c === lab.wyjscie.c) d.classList.add("lb-wyjscie");
      }
    }

    host.querySelector(".lb-kroki").textContent = s.kroki;
    host.querySelector(".lb-kroki-sl").textContent = odmien(s.kroki, "krok", "kroki", "kroków");
    host.querySelector(".lb-odw").textContent = s.odwiedzone.size;
    host.querySelector(".lb-odw-sl").textContent = POLA(s.odwiedzone.size);
    const dl = host.querySelector(".lb-dlugosc");
    dl.hidden = !s.sciezka;
    if (s.sciezka) {
      host.querySelector(".lb-dl").textContent = s.sciezka.length;
      host.querySelector(".lb-dl-sl").textContent = POLA(s.sciezka.length);
    }

    // Pogrubienia z opisu (**tekst**) zamieniamy na <strong> — opisy piszemy
    // w tej samej konwencji co resztę materiału.
    host.querySelector(".lb-opis").innerHTML = s.opis
      .replace(/[&<>]/g, (z) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[z]))
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

    host.querySelector(".lb-etykieta").textContent =
      s.tryb === "dfs" ? "Stos (wierzch po prawej):" : "Kolejka (wychodzi z lewej):";
    const lista = s.pojemnik.map((p) => `${p.r},${p.c}`);
    const skrot = lista.length > 12
      ? `… ${lista.slice(-12).join("  ")}`
      : (lista.join("  ") || "pusty");
    host.querySelector(".lb-zawartosc").textContent = skrot;

    host.querySelectorAll(".lb-tryb").forEach((b) =>
      b.classList.toggle("lb-wybrany", b.dataset.tryb === s.tryb));
    host.querySelector(".lb-krok").disabled = s.koniec;
    host.querySelector(".lb-graj").disabled = s.koniec;
  }

  /* ───────────────────────────────────────────────────── montaż */
  function uruchom(host) {
    if (host.dataset.gotowe) return;
    host.dataset.gotowe = "1";

    const dane = JSON.parse(host.querySelector("script[type='application/json']").textContent);
    let lab;
    try {
      lab = wczytaj(dane.siatka);
    } catch (e) {
      host.innerHTML = `<p class="lb-blad">Nie udało się wczytać labiryntu: ${e.message}</p>`;
      return;
    }

    const widok = zbuduj(host, lab, dane.tryb);
    let s = nowyStan(lab, dane.tryb === "bfs" ? "bfs" : "dfs");
    let timer = null;

    const stop = () => { clearInterval(timer); timer = null; host.querySelector(".lb-graj").textContent = "Do końca"; };
    const rysuj = () => odswiez(host, lab, s, widok);

    host.querySelector(".lb-krok").addEventListener("click", () => {
      stop(); krok(lab, s); rysuj();
    });

    host.querySelector(".lb-graj").addEventListener("click", (e) => {
      if (timer) { stop(); return; }
      e.currentTarget.textContent = "Zatrzymaj";
      timer = setInterval(() => {
        krok(lab, s); rysuj();
        if (s.koniec) stop();
      }, 110);
    });

    host.querySelector(".lb-reset").addEventListener("click", () => {
      stop(); s = nowyStan(lab, s.tryb); rysuj();
    });

    host.querySelectorAll(".lb-tryb").forEach((b) =>
      b.addEventListener("click", () => {
        stop(); s = nowyStan(lab, b.dataset.tryb); rysuj();
      }));

    rysuj();
  }

  function start() {
    document.querySelectorAll(".labirynt").forEach(uruchom);
  }

  // navigation.instant podmienia treść bez przeładowania strony, więc
  // montujemy się na document$, a nie na DOMContentLoaded.
  if (typeof document$ !== "undefined") document$.subscribe(start);
  else document.addEventListener("DOMContentLoaded", start);
})();
