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
st.write("Welcome Hero! XP can only be earned by completing challenges.")

# -----------------------------
# DATA
# -----------------------------
characters = {
    "Pokemon": {
        "Pikachu": "Electric mouse with thunder power ⚡",
        "Charizard": "Fire-breathing dragon 🔥",
        "Eevee": "Evolution master 🌟"
    },
    "Wings of Fire": {
        "Clay": "Strong MudWing 🐉",
        "Glory": "RainWing queen 🐍",
        "Sunny": "Bright SandWing ☀️"
    },
    "LEGO": {
        "Kai": "Fire ninja 🔴",
        "Lloyd": "Green ninja 🟢",
        "Zane": "Ice robot 🤖"
    },
    "Mario": {
        "Mario": "Hero of Mushroom Kingdom 🍄",
        "Luigi": "Brave brother 👻",
        "Yoshi": "Dino companion 🦖"
    }
}

# -----------------------------
# SESSION STATE
# -----------------------------
if "xp" not in st.session_state:
    st.session_state.xp = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "challenge_done" not in st.session_state:
    st.session_state.challenge_done = {}

# -----------------------------
# UNIVERSE + CHARACTER
# -----------------------------
universe = st.selectbox("Choose Universe 🌍", list(characters.keys()))
character = st.selectbox("Choose Character 👤", list(characters[universe].keys()))

st.subheader(f"{character} from {universe}")
st.info(characters[universe][character])

# -----------------------------
# CHALLENGE SYSTEM
# -----------------------------
st.write("## ⚔️ Challenges (Complete to earn XP)")

challenges = {
    "Pokemon": [
        ("⚡ Thunder Focus Test", "Answer: Pikachu is an Electric type", "electric"),
        ("🔥 Fire Knowledge Trial", "Which type beats Fire?", "water"),
        ("🌿 Evolution Puzzle", "Eevee evolves into how many main forms?", "8")
    ],
    "Wings of Fire": [
        ("🐉 Dragon Loyalty Test", "Clay is part of which tribe?", "mudwing"),
        ("🌈 RainWing Riddle", "Glory belongs to which tribe?", "rainwing"),
        ("☀️ Desert Survival", "Sunny is a...?", "sandwing")
    ],
    "LEGO": [
        ("🔴 Fire Trial", "Kai controls what element?", "fire"),
        ("🟢 Leadership Test", "Who is the Green Ninja?", "lloyd"),
        ("🤖 Ice Logic", "Zane is part human or robot?", "robot")
    ],
    "Mario": [
        ("🍄 Mushroom Quiz", "Who is Mario’s brother?", "luigi"),
        ("👻 Ghost House", "Luigi is known for being?", "brave"),
        ("🦖 Dino Friend", "Yoshi is what kind of creature?", "dino")
    ]
}

selected_challenges = challenges[universe]

# -----------------------------
# DISPLAY CHALLENGES
# -----------------------------
for i, (title, question, answer) in enumerate(selected_challenges):
    st.write(f"### {title}")
    st.write(question)

    key = f"{universe}_{i}"

    if key not in st.session_state.challenge_done:
        user_input = st.text_input(f"Your answer for Challenge {i+1}", key=key)

        if st.button(f"Submit Challenge {i+1}", key=f"btn_{key}"):
            if user_input.lower().strip() == answer:
                st.success("Correct! +20 XP 🎉")
                st.session_state.xp += 20
                st.session_state.challenge_done[key] = True

                st.session_state.history.append(
                    f"{character} completed '{title}' in {universe}"
                )
            else:
                st.error("Wrong answer! Try again ❌")

    else:
        st.success("Completed ✅")

# -----------------------------
# XP SYSTEM
# -----------------------------
st.write("## ⭐ Progress")

st.metric("XP", st.session_state.xp)
st.progress((st.session_state.xp % 100) / 100)

# -----------------------------
# JOURNEY LOG
# -----------------------------
st.write("## 📜 Adventure Log")

if st.session_state.history:
    for h in reversed(st.session_state.history):
        st.write("•", h)
else:
    st.write("No completed challenges yet...")

# -----------------------------
# STATS PANEL
# -----------------------------
st.write("## 📊 World Stats")

col1, col2 = st.columns(2)

with col1:
    st.metric("Universe", universe)

with col2:
    st.metric("Challenges Available", len(selected_challenges))
