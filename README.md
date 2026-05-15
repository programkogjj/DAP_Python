# Výuka programování v Pythonu pomocí Sonic Pi

Tento repozitář obsahuje materiály, zdrojové kódy a interaktivní aplikaci pro vzdělávací projekt zaměřený na výuku programování v jazyce Python skrze algoritmickou kompozici hudby.

## 🎯 Zaměření projektu

Práce se zabývá využitím hudebního programovacího prostředí **Sonic Pi** a knihovny **psonic** jako motivačního nástroje pro výuku programování. Projekt porovnává efektivitu výuky v čistém Pythonu oproti interaktivní hudební tvorbě (experimentální vs. kontrolní skupina).
Webová aplikace se zpětnou vazbou ke cvičením je dostupná na: https://dappython-forstudents.streamlit.app/

## 📊 Struktura projektu a úložiště


| Soubor / Složka | Popis a účel |
| :--- | :--- |
| **`Home.py`** | Vstupní bod Streamlit aplikace; obsahuje úvodní text a navigaci kurzu. |
| **`pages/`** | Skripty definující funkčnost a vizuální stránku jednotlivých podstránek webové aplikace Streamlit. |
| **`Python_SonicPi/`** | Interaktivní výukové lekce zaměřené na algoritmickou kompozici hudby pomocí knihovny *psonic* a nástroje Sonic Pi. |
| **`Python/`** | Výukové materiály v čistém Pythonu (prázdné i vyplněné verze 1–6) pro kontrolní skupinu. |
| **`psonic_working.rb`** | Konfigurační skript pro Sonic Pi. |
| **`Sounds/`** | Strukturované úložiště (`.wav`/`.flac`) vygenerovaných zvuků sloužící pro kontrolu výsledků cvičení pro experimentální skupinu. |
| **`manual_*.pdf`** | Uživatelské příručky pro zprovoznění kurzu v lokálním prostředí (*exp* – experimentální skupina, *con* – kontrolní skupina). |
| **`Posttest_*.pdf`** | Závěrečné testy (PostTest) po ukončení kurzu pro obě skupiny. |
| **`midi_board.png`** | Grafické schéma klaviatury/ovladače využité v rozhraní aplikace. |
