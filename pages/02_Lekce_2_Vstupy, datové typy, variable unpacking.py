import streamlit as st
import os

# Definujeme cestu ke složce se zvuky
SOUNDS_DIR = "sounds"

def play_sound(filename):
    path = os.path.join(SOUNDS_DIR, filename)
    if os.path.exists(path):
        st.audio(path)
    else:
        st.error(f"Soubor {filename} nebyl nalezen v adresáři {SOUNDS_DIR}")

st.title("Lekce 2 - Vstupy, datové typy, rozbalování kolekce, ")

import streamlit as st
import os


st.markdown("""
V této lekci se naučíme získávat data od uživatele pomocí interaktivních výzev, pochopíme rozdíly mezi datovými typy a naučíme se rozdělovat složitější řetězce.
""")

st.divider()

## --- Kapitola 2.1 ---
st.header("2.1 Vstup uživatele")
st.write("V Pythonu používáme pro získání vstupu funkci `input()`. Ve Streamlitu pro tento účel slouží různé widgety.")

### Cvičení 2.1.1
st.subheader("Cvičení 2.1.1: Součet z výzvy")
st.markdown("Načtení dvou čísel a jejich následný součet.")
if st.button("Poslechnout Součet"):
    # Předpokládaný výsledek ton_1(20) + ton_2(30)
    play_sound("cvic2_1_1.wav")

### Cvičení 2.1.2
st.subheader("Cvičení 2.1.2: Tón součinem")
if st.button("Poslechnout Součin tónů"):
    play_sound("cvic2_1_2.wav")

st.divider()

## --- Kapitola 2.2 ---
st.header("2.2 Přetypování")
st.write("Změna datového typu pomocí funkcí `int()`, `float()` a `str()`.")

### Cvičení 2.2.1
st.subheader("Cvičení 2.2.1: Desetinná čísla")
col1, col2 = st.columns(2)
with col1:
    if st.button("Pauza jako celé číslo (int)"):
        play_sound("cvic2_2_1_int.wav")
with col2:
    if st.button("Pauza jako desetinné (float)"):
        play_sound("cvic2_2_1_float.wav")

### Cvičení 2.2.2
st.subheader("Cvičení 2.2.2: Procvičení přetypování")
if st.button("Poslechnout výsledek celočíselného podílu"):
    play_sound("cvic2_2_2.wav")

### Cvičení 2.2.3
st.subheader("Cvičení 2.2.3: Zahraj náhodný tón")
st.write("Použití modulu `random` pro generování náhodné výšky tónu.")
if st.button("Přehrát náhodný výběr"):
    play_sound("cvic2_2_3.wav")

st.divider()

## --- Kapitola 2.3 ---
st.header("2.3 Rozdělení řetězce")
st.write("Použití metody `.split()` pro zpracování více hodnot zadaných najednou.")

### Cvičení 2.3.1
st.subheader("Cvičení 2.3.1: Jednoduchý separátor (středník)")
if st.button("Poslechnout separované tóny"):
    play_sound("cvic2_3_1.wav")

### Cvičení 2.3.2
st.subheader("Cvičení 2.3.2: Víceznakový separátor")
if st.button("Poslechnout víceznakový separátor"):
    play_sound("cvic2_3_2.wav")

st.subheader("Cvičení 2.3.3: složitý separátor")
if st.button("Poslechnout složitý separátor"):
    play_sound("cvic2_3_3.wav")

st.subheader("Cvičení 2.3.4")
st.write("Kombinace načtení tónů a náhodnost")
if st.button("Poslechnout sekvenci"):
    play_sound("cvic2_4_4.wav")

st.divider()