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

st.title("Lekce 3 - Rozhodování a logické výrazy")

st.markdown("""
V této lekci se naučíme, jak ovlivňovat průběh programu a výsledný zvuk pomocí podmínek `if`, `elif` a `else`.
""")

st.divider()

st.image("midi_board.png", caption="hodnoty tónů v MIDI")

## --- Kapitola 3.1 ---
st.header("3.1 Podmínka IF")

### Cvičení 3.1.1a
st.subheader("Cvičení 3.1.1a: Jsi hudebník?")
st.info("Předaná hodnota: 'ano'")
if st.button("Přehrát 3.1.1a"):
    play_sound("l3/cvic3_1_1a.wav")

### Cvičení 3.1.2
st.subheader("Cvičení 3.1.2: Vítěz závodu")
st.info("Předaná hodnota: hodnota menší než hodnota rekordu")
if st.button("Přehrát 3.1.2"):
    play_sound("l3/cvic3_1_2.wav")

### Cvičení 3.1.3
st.subheader("Cvičení 3.1.3: Lepší hráč")
st.info("Předaná hodnota: první skóre vyšší než druhé skóre (zahrán tón C4)")
if st.button("Přehrát 3.1.3"):
    play_sound("l3/cvic3_1_3.wav")

### Cvičení 3.1.4
st.subheader("Cvičení 3.1.4: Hudební styly")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info("Věk = 6")
    if st.button("Přehrát 3.1.4a"):
        play_sound("l3/cvic3_1_4a.wav")
with col2:
    st.info("Věk = 17")
    if st.button("Přehrát 3.1.4b"):
        play_sound("l3/cvic3_1_4b.wav")
with col3:
    st.info("Věk = 30")
    if st.button("Přehrát 3.1.4c"):
        play_sound("l3/cvic3_1_4c.wav")
with col4:
    st.info("Věk = 65")
    if st.button("Přehrát 3.1.4d"):
        play_sound("l3/cvic3_1_4d.wav")

st.divider()

## --- Kapitola 3.3 ---
st.header("3.3 Větvení programu (If - Else, Elif)")

### Cvičení 3.3.1
st.subheader("Cvičení 3.3.1: Dynamika tónu")
col1, col2 = st.columns(2)
with col1:
    st.info("Hlasitost: 0.8, Volba: 'bici'")
    if st.button("Přehrát 3.3.1a"):
        play_sound("l3/cvic3_3_1a.wav")
with col2:
    st.info("Hlasitost: 0.5, Volba: 'ton'")
    if st.button("Přehrát 3.3.1b"):
        play_sound("l3/cvic3_3_1b.wav")

### Cvičení 3.3.2
st.subheader("Cvičení 3.3.2: Jakou máš náladu?")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info("'rock', 'vesela'")
    if st.button("Přehrát 3.3.2a"):
        play_sound("l3/cvic3_3_2a.wav")
with col2:
    st.info("'rock', 'smutna'")
    if st.button("Přehrát 3.3.2b"):
        play_sound("l3/cvic3_3_2b.wav")
with col3:
    st.info("'klasika', 'vesela'")
    if st.button("Přehrát 3.3.2c"):
        play_sound("l3/cvic3_3_2c.wav")
with col4:
    st.info("'klasika', 'smutna'")
    if st.button("Přehrát 3.3.2d"):
        play_sound("l3/cvic3_3_2d.wav")

### Cvičení 3.3.3
st.subheader("Cvičení 3.3.3: Limitér hlasitosti")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("Intenzita = 200")
    if st.button("Přehrát 3.3.3a"):
        play_sound("l3/cvic3_3_3a.wav")
with col2:
    st.info("Intenzita = 50")
    if st.button("Přehrát 3.3.3b"):
        play_sound("l3/cvic3_3_3b.wav")
with col3:
    st.info("Intenzita = 0")
    if st.button("Přehrát 3.3.3c"):
        play_sound("l3/cvic3_3_3c.wav")

### Cvičení 3.3.4
st.subheader("Cvičení 3.3.4: Hudební žebříček")
st.info("Předané hodnoty: 50, 70, 65")
if st.button("Přehrát 3.3.4"):
    play_sound("l3/cvic3_3_4.wav")

st.divider()

## --- Kapitola 3.4 ---
st.header("3.4 Komplexní rozhodování")

### Cvičení 3.4.2
st.subheader("Cvičení 3.4.2: Koncert")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("Počet chyb = 5")
    if st.button("Přehrát (5 chyb)"):
        play_sound("l3/cvic3_4_2a.wav")
with col2:
    st.info("Počet chyb = 2")
    if st.button("Přehrát (2 chyby)"):
        play_sound("l3/cvic3_4_2b.wav")
with col3:
    st.info("Počet chyb = 0")
    if st.button("Přehrát (0 chyb)"):
        play_sound("l3/cvic3_4_2c.wav")

st.divider()