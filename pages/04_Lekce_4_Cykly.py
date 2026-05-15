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

st.title("Lekce 4 - Cykly")

st.markdown("""
V této lekci se naučíme, jak zadat programu příkaz k opakování sekvence příkazů.
""")

st.divider()
st.image("midi_board.png", caption="hodnoty tónů v MIDI")

## --- Kapitola 4.1 ---
st.header("4.1 Cyklus se známým počtem opakování (FOR)")

### Cvičení 4.1.1
st.subheader("Cvičení 4.1.1: Bubeník")
if st.button("Přehrát 4.1.1"):
    play_sound("l4/cvic4_1_1.wav")

### Cvičení 4.1.2
st.subheader("Cvičení 4.1.2: Hudebníkův nástroj")
st.info("Předané hodnoty: piano (chyba), kytara (správně)")
if st.button("Přehrát 4.1.2"):
    play_sound("l4/cvic4_1_2.wav")

### Cvičení 4.1.3
st.subheader("Cvičení 4.1.3: Parametry našeho riffu")
st.info("Předané hodnoty: start = 50, konec = 70, krok = 2")
if st.button("Přehrát 4.1.3"):
    play_sound("l4/cvic4_1_3.wav")

### Cvičení 4.1.4
st.subheader("Cvičení 4.1.4: Fade-out")
if st.button("Přehrát 4.1.4"):
    play_sound("l4/cvic4_1_4.wav")

### Cvičení 4.1.5
st.subheader("Cvičení 4.1.5: Stereo rytmus (Sudá a lichá)")
if st.button("Přehrát 4.1.5"):
    play_sound("l4/cvic4_1_5.wav")

st.divider()

## --- Kapitola 4.2 ---
st.header("4.2 Cyklus s podmínkou na začátku (WHILE)")

### Cvičení 4.2.1
st.subheader("Cvičení 4.2.1: Basová linka")
if st.button("Přehrát 4.2.1"):
    play_sound("l4/cvic4_2_1.wav")

### Cvičení 4.2.2
st.subheader("Cvičení 4.2.2: Metronom")
if st.button("Přehrát 4.2.2"):
    play_sound("l4/cvic4_2_2.wav")

### Cvičení 4.2.3
st.subheader("Cvičení 4.2.3: Zvukový filtr")
if st.button("Přehrát 4.2.3"):
    play_sound("l4/cvic4_2_3.wav")

### Cvičení 4.2.4
st.subheader("Cvičení 4.2.4: Ze strany na stranu")
if st.button("Přehrát 4.2.4"):
    play_sound("l4/cvic4_2_4.wav")

st.divider()

## --- Kapitola 4.3 ---
st.header("4.3 Cykly a kolekce")

### Cvičení 4.3.1
st.subheader("Cvičení 4.3.1: Testujeme hudební sluch")
st.info("Předané hodnoty: 60, 62, 63")
if st.button("Přehrát 4.3.1"):
    play_sound("l4/cvic4_3_1.wav")

### Cvičení 4.3.2
st.subheader("Cvičení 4.3.2: Přeskoč hodnoty")
if st.button("Přehrát 4.3.2"):
    play_sound("l4/cvic4_3_2.wav")

### Cvičení 4.3.3
st.subheader("Cvičení 4.3.3: Vytvoř akord")
st.info("Předané hodnoty: 60, 55, 64")
if st.button("Přehrát 4.3.3"):
    play_sound("l4/cvic4_3_3.wav")

st.divider()

## --- Kapitola 4.4 ---
st.header("4.4 Vnořené cykly")

### Cvičení 4.4.1
st.subheader("Cvičení 4.4.1: Dvojný cyklus")
if st.button("Přehrát 4.4.1"):
    play_sound("l4/cvic4_4_1.wav")

### Cvičení 4.4.2
st.subheader("Cvičení 4.4.2: Dvojný While cyklus")
if st.button("Přehrát 4.4.2"):
    play_sound("l4/cvic4_4_2.wav")

st.divider()