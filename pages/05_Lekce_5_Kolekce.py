import streamlit as st
import os

# Definujeme cestu ke složce se zvuky
SOUNDS_DIR = "Sounds"

def play_sound(filename):
    path = os.path.join(SOUNDS_DIR, filename)
    if os.path.exists(path):
        st.audio(path)
    else:
        st.error(f"Soubor {filename} nebyl nalezen v adresáři {SOUNDS_DIR}")

st.title("Lekce 5 - Kolekce")

st.markdown("""
V této lekci se seznámíte s kolekcemi (seznamy), které umožňují uchovávat více hodnot najednou, a naučíte se je procházet a zpracovávat pomocí cyklů.
""")

st.divider()
st.image("midi_board.png", caption="hodnoty tónů v MIDI")

## --- Kapitola 5.1 ---
st.header("5.1 Práce se seznamy a agregace")

### Cvičení 5.1.1
st.subheader("Cvičení 5.1.1: Načtení desetinných čísel")
st.info("Předané hodnoty: 60.5, 70.6, 66.75")
if st.button("Přehrát 5.1.1"):
    play_sound("l5/cvic5_1_1.wav")

### Cvičení 5.1.2
st.subheader("Cvičení 5.1.2: Poslední zadaný prvek")
st.info("Předané hodnoty: 60, 65, 70, 55")
if st.button("Přehrát 5.1.2"):
    play_sound("l5/cvic5_1_2.wav")

### Cvičení 5.1.3
st.subheader("Cvičení 5.1.3: Použij hodnoty kolekce")
if st.button("Přehrát 5.1.3"):
    play_sound("l5/cvic5_1_3.wav")

### Cvičení 5.1.4
st.subheader("Cvičení 5.1.4: Součin prvků z kolekce")
if st.button("Přehrát 5.1.4"):
    play_sound("l5/cvic5_1_4.wav")

### Cvičení 5.1.5
st.subheader("Cvičení 5.1.5: Průměrná výška melodie")
if st.button("Přehrát 5.1.5"):
    play_sound("l5/cvic5_1_5.wav")

### Cvičení 5.1.6
st.subheader("Cvičení 5.1.6: Smysluplná hodnota")
if st.button("Přehrát 5.1.6"):
    play_sound("l5/cvic5_1_6.wav")

st.divider()

## --- Kapitola 5.2 ---
st.header("5.2 Vyhledávání a extrémy")

### Cvičení 5.2.1
st.subheader("Cvičení 5.2.1: Najdi index hledaného prvku")
if st.button("Přehrát 5.2.1"):
    play_sound("l5/cvic5_2_1.wav")

### Cvičení 5.2.2
st.subheader("Cvičení 5.2.2: Jaké číslo hledáme?")
col1, col2 = st.columns(2)
with col1:
    st.info("Hledaná hodnota: 31")
    if st.button("Přehrát 5.2.2a"):
        play_sound("l5/cvic5_2_2a.wav")
with col2:
    st.info("Hledaná hodnota: 69")
    if st.button("Přehrát 5.2.2b"):
        play_sound("l5/cvic5_2_2b.wav")

### Cvičení 5.2.3
st.subheader("Cvičení 5.2.3: Vyhledání indexu maxima")
if st.button("Přehrát 5.2.3"):
    play_sound("l5/cvic5_2_3.wav")

### Cvičení 5.2.4
st.subheader("Cvičení 5.2.4: Vyhledání minima")
if st.button("Přehrát 5.2.4"):
    play_sound("l5/cvic5_2_4.wav")

st.divider()

## --- Kapitola 5.3 ---
st.header("5.3 Algoritmy a řazení")

### Cvičení 5.3.2
st.subheader("Cvičení 5.3.2: Prohození obsahu proměnných")
st.info("Předané hodnoty: první tón = 60, druhý tón = 70")
if st.button("Přehrát 5.3.2"):
    play_sound("l5/cvic5_3_2.wav")

### Cvičení 5.3.3
st.subheader("Cvičení 5.3.3: Procházení dvojic")
if st.button("Přehrát 5.3.3"):
    play_sound("l5/cvic5_3_3.wav")

### Cvičení 5.3.4
st.subheader("Cvičení 5.3.4: Prohazování dvojic")
if st.button("Přehrát 5.3.4"):
    play_sound("l5/cvic5_3_4.wav")

### Cvičení 5.3.5
st.subheader("Cvičení 5.3.5: Neoptimalizované Bublinkové třídění")
if st.button("Přehrát 5.3.5"):
    play_sound("l5/cvic5_3_5.wav")

### Cvičení 5.3.7
st.subheader("Cvičení 5.3.7: Seřaď sestupně")
st.info("Algoritmus seřadil hodnoty od největší po nejmenší.")
if st.button("Přehrát 5.3.7"):
    play_sound("l5/cvic5_3_7.wav")

st.divider()