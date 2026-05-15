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

st.title("Lekce 2 - Vstupy, datové typy a kolekce")

st.markdown("""
V této lekci se naučíme, jak získávat data od uživatele pomocí `input()`, jak pracovat s různými datovými typy a jak rozdělovat řetězce.
""")

st.divider()

st.image("midi_board.png", caption="hodnoty tónů v MIDI")

## --- Kapitola 2.1 ---
st.header("2.1 Vstup uživatele")

### Cvičení 2.1.1
st.subheader("Cvičení 2.1.1: Součet z výzvy")
st.info("Předané hodnoty: 20 a 30")
if st.button("Poslechnout výsledek 2.1.1"):
    play_sound("l2/cvic2_1_1.wav")

### Cvičení 2.1.2
st.subheader("Cvičení 2.1.2: Tón součinem")
st.info("Předané hodnoty: 2 a 30")
if st.button("Poslechnout výsledek 2.1.2"):
    play_sound("l2/cvic2_1_2.wav")

st.divider()

## --- Kapitola 2.2 ---
st.header("2.2 Přetypování")

### Cvičení 2.2.1
st.subheader("Cvičení 2.2.1: Desetinná čísla")
st.info("Práce s hodnotou 1.6")
col1, col2 = st.columns(2)
if st.button("Poslechnout výsledek 2.2.1:"):
    play_sound("l2/cvic2_2_1.wav")

### Cvičení 2.2.2
st.subheader("Cvičení 2.2.2: Procvičení přetypování")
st.info("Předané hodnoty: 150 a 2")
if st.button("Poslechnout výsledek 2.2.2"):
    play_sound("l2/cvic2_2_2.wav")

### Cvičení 2.2.3
st.subheader("Cvičení 2.2.3: Zahraj náhodný tón")
st.info("Předané rozmezí: 40 a 100")
if st.button("Přehrát náhodný tón"):
    play_sound("l2/cvic2_2_3.wav")

st.divider()

## --- Kapitola 2.3 ---
st.header("2.3 Rozdělení řetězce")

### Cvičení 2.3.1
st.subheader("Cvičení 2.3.1: Jednoduchý separátor")
if st.button("Poslechnout 2.3.1"):
    play_sound("l2/cvic2_3_1.wav")

### Cvičení 2.3.2
st.subheader("Cvičení 2.3.2: Víceznakový separátor")
if st.button("Poslechnout 2.3.2"):
    play_sound("l2/cvic2_3_2.wav")

### Cvičení 2.3.3
st.subheader("Cvičení 2.3.3: Složitý separátor")
if st.button("Poslechnout 2.3.3"):
    play_sound("l2/cvic2_3_3.wav")

### Cvičení 2.3.4
st.subheader("Cvičení 2.3.4: Načtení tónů")
st.info("Předané hodnoty: 40, 50, 60, 65, 70")
if st.button("Přehrát sekvenci 2.3.4"):
    play_sound("l2/cvic2_3_4.wav")

### Cvičení 2.3.5
st.subheader("Cvičení 2.3.5: Náhodné elementy")
st.info("Předané hodnoty: 40, 50, 60, 65, 70 (náhodná pauza, pan a amp)")
if st.button("Přehrát 2.3.5"):
    play_sound("l2/cvic2_3_5.wav")

st.divider()