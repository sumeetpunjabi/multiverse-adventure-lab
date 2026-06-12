import streamlit as st

st.set_page_config(
    page_title="Multiverse Adventure Lab",
    page_icon="🌌"
)

st.title("🌌 Multiverse Adventure Lab")

st.write(
    """
Welcome Hero!

Choose a universe and meet your characters.
"""
)

universe = st.selectbox(
    "Choose a Universe",
    [
        "Pokemon",
        "Wings of Fire",
        "LEGO",
        "Mario"
    ]
)

characters = {
    "Pokemon": [
        "Pikachu",
        "Charizard",
        "Eevee"
    ],
    "Wings of Fire": [
        "Clay",
        "Glory",
        "Sunny"
    ],
    "LEGO": [
        "Kai",
        "Lloyd",
        "Zane"
    ],
    "Mario": [
        "Mario",
        "Luigi",
        "Yoshi"
    ]
}

st.subheader("Characters")

for c in characters[universe]:
    st.write("⭐", c)
