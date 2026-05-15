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

st.title("Lekce 6 - Vlastní funkce")

st.markdown("""
V této lekci se naučíme definovat vlastní funkce, které nám umožní lépe strukturovat kód, eliminovat opakování a vytvářet znovupoužitelné hudební nástroje.
""")

st.divider()
st.image("midi_board.png", caption="hodnoty tónů v MIDI")

## --- Kapitola 6.1 ---
st.header("6.1 Definice funkcí a parametry")

### Cvičení 6.1.1
st.subheader("Cvičení 6.1.1: Harmonický součin")
st.info("Předané hodnoty: vypocitej_ton(5, 10, 4)")
if st.button("Přehrát 6.1.1"):
    play_sound("l6/cvic6_1_1.wav")

### Cvičení 6.1.2
st.subheader("Cvičení 6.1.2: Lineární modulace")
st.info("Předané hodnoty: zavisla_promenna(10, -3, 9)")
if st.button("Přehrát 6.1.2"):
    play_sound("l6/cvic6_1_2.wav")

### Cvičení 6.1.3
st.subheader("Cvičení 6.1.3: Detektor Zlatého řezu")
st.info("Předané hodnoty: a = 10, b = 7")
if st.button("Přehrát 6.1.3"):
    play_sound("l6/cvic6_1_3.wav")

### Cvičení 6.1.4
st.subheader("Cvičení 6.1.4: Vlastní funkce k vyhledání maxima")
if st.button("Přehrát 6.1.4"):
    play_sound("l6/cvic6_1_4.wav")

### Cvičení 6.1.5
st.subheader("Cvičení 6.1.5: Generátor intervalových zrcadel")
col1, col2 = st.columns(2)
with col1:
    st.info("Základ = 70, Posun = 5")
    if st.button("Přehrát 6.1.5a"):
        play_sound("l6/cvic6_1_5a.wav")
with col2:
    st.info("Základ = 70, Posun = defaultní")
    if st.button("Přehrát 6.1.5b"):
        play_sound("l6/cvic6_1_5b.wav")

### Cvičení 6.1.6
st.subheader("Cvičení 6.1.6: Chytrý příkaz play")
col1, col2 = st.columns(2)
with col1:
    st.info("Spuštění s defaultními hodnotami")
    if st.button("Přehrát 6.1.6a"):
        play_sound("l6/cvic6_1_6a.wav")
with col2:
    st.info("ton = 70, stranovost = 1, trvani = 0.5")
    if st.button("Přehrát 6.1.6b"):
        play_sound("l6/cvic6_1_6b.wav")

st.divider()

## --- Kapitola 6.2 ---
st.header("6.2 Návratové hodnoty a dokumentace")

### Cvičení 6.2.1
st.subheader("Cvičení 6.2.1: Dokumentace hudební funkce")
st.info("Předané hodnoty: nota = 70, síla = 20")
if st.button("Přehrát 6.2.1"):
    play_sound("l6/cvic6_2_1.wav")

### Cvičení 6.2.2
st.subheader("Cvičení 6.2.2: Binární variace")
st.info("předané tóny [60,64,67,72,66,73,71]")
if st.button("Přehrát 6.2.2"):
    play_sound("l6/cvic6_2_2.wav")

### Cvičení 6.2.3
st.subheader("Cvičení 6.2.3: Analýza hudebního rozsahu")
st.info("předané tóny [60,64,67,72,66,73,71]")
if st.button("Přehrát 6.2.3"):
    play_sound("l6/cvic6_2_3.wav")

### Cvičení 6.2.4
st.subheader("Cvičení 6.2.4: Bezpečnostní filtr")
if st.button("Přehrát 6.2.4"):
    play_sound("l6/cvic6_2_4.wav")

st.divider()