import streamlit as st
import random

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Multiverse Adventure Lab",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Multiverse Adventure Lab")

st.write("Welcome Hero! Explore universes, meet characters, and create your story.")

# -----------------------------
# DATA
# -----------------------------
characters = {
    "Pokemon": {
        "Pikachu": "Electric mouse with thunder power ⚡",
        "Charizard": "Fire-breathing dragon lizard 🔥",
        "Eevee": "Evolution master with many forms 🌟"
    },
    "Wings of Fire": {
        "Clay": "Strong and loyal MudWing 🐉",
        "Glory": "RainWing queen with venom strike 🐍",
        "Sunny": "Optimistic SandWing ☀️"
    },
    "LEGO": {
        "Kai": "Fire ninja of speed 🔴",
        "Lloyd": "Green ninja leader 🟢",
        "Zane": "Ice-powered robot 🤖"
    },
    "Mario": {
        "Mario": "Hero of the Mushroom Kingdom 🍄",
        "Luigi": "Brave but nervous brother 👻",
        "Yoshi": "Dino companion with a big heart 🦖"
    }
}

# -----------------------------
# UNIVERSE SELECT
# -----------------------------
universe = st.selectbox(
    "Choose a Universe 🌍",
    list(characters.keys())
)

st.subheader(f"Welcome to {universe}")

# -----------------------------
# CHARACTER SELECT
# -----------------------------
selected_character = st.selectbox(
    "Pick your character",
    list(characters[universe].keys())
)

st.write("### Character Profile")
st.info(characters[universe][selected_character])

# -----------------------------
# ACTION SYSTEM
# -----------------------------
st.write("## 🎮 Actions")

action = st.radio(
    "What do you want to do?",
    ["Talk", "Train", "Adventure"]
)

if action == "Talk":
    st.success(f"{selected_character} says: 'Hello traveler from {universe}!' 🗣️")

elif action == "Train":
    st.warning(f"{selected_character} is powering up... training arc activated 💪⚡")

elif action == "Adventure":
    st.error(f"{selected_character} enters a dangerous quest in {universe} 🌌🔥")

# -----------------------------
# RANDOM EVENTS
# -----------------------------
st.write("## 🎲 Random Events")

if st.button("Trigger Event"):
    events = [
        "A wild challenge appears!",
        "You discovered a hidden power-up!",
        "A rival appears from another universe!",
        "Legendary artifact found!",
        "Time distortion detected... reality shifts!"
    ]
    st.info(random.choice(events))

# -----------------------------
# XP SYSTEM (SESSION STATE)
# -----------------------------
if "xp" not in st.session_state:
    st.session_state.xp = 0

st.write("## ⭐ Progress")

col1, col2 = st.columns(2)

with col1:
    if st.button("Gain XP"):
        st.session_state.xp += 10

with col2:
    st.write("Current XP:")
    st.metric("XP", st.session_state.xp)

st.progress((st.session_state.xp % 100) / 100)

# -----------------------------
# JOURNEY LOG
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Save Adventure"):
    st.session_state.history.append(
        f"{selected_character} in {universe} doing {action}"
    )

st.write("## 📜 Your Journey Log")

if st.session_state.history:
    for h in st.session_state.history[::-1]:
        st.write("•", h)
else:
    st.write("No adventures yet... start your journey!")

# -----------------------------
# STATS PANEL
# -----------------------------
st.write("## 📊 World Stats")

col3, col4 = st.columns(2)

with col3:
    st.metric("Universe", universe)

with col4:
    st.metric("Characters", len(characters[universe]))
