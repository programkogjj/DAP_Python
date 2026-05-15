import streamlit as st


# Úvodní text pro studenty
st.markdown("""
# Vítejte v kurzu Programování s Pythonem a Sonic Pi 🎹

Vítejte v kurzu programování a algoritmizace, který je navržen tak, aby vás naučil základy programování v **Pythonu** netradiční a zábavnou formou – skrze tvorbu **hudby a zvuků** v reálném čase pomocí platformy **Sonic Pi**.

---

### 🚀 Co vás v tomto kurzu čeká?

* **Algoritmické myšlení:** Naučíte se přemýšlet jako programátoři a zapisovat své nápady do kódu tak, aby je počítač správně vykonal.
* **Základy Pythonu:** Prozkoumáme proměnné, aritmetické operace, funkce a datové struktury, podmínky a cykly.
* **Hudební informatika:** Zjistíte, jak se pomocí kódu tvoří tóny, akordy a rytmické sekvence.

### 🛠️ Jak s aplikací pracovat?
""")
st.markdown("##### Manuál k zprovoznění prostředí programování (PDF)")

try:
    with open("manual_exp.pdf", "rb") as file:
        st.download_button(
            label="Stáhnout",  # Text přímo na tlačítku
            data=file,
            file_name="manual_pro_zprovozneni.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("Soubor manual_exp.pdf nebyl nalezen.")

st.markdown("""
1. **Mějte spuštěné Sonic Pi:** Aby vše fungovalo, musí vám na pozadí běžet program Sonic Pi.
2. **Procházejte lekce:** Každá kapitola obsahuje teoretický úvod a interaktivní cvičení.
3. **Tvořte a poslouchejte:** U každého cvičení najdete tlačítko **"Play"**, k ověření správnosti vašeho řešení.

---
**Pojďme společně do lekce lekce 1 rozeznít váš první řádek kódu!**
""")