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
st.write("Welcome Hero! Only true explorers can unlock XP.")

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

if "done" not in st.session_state:
    st.session_state.done = {}

# -----------------------------
# UNIVERSE + CHARACTER
# -----------------------------
universe = st.selectbox("Choose Universe 🌍", list(characters.keys()))
character = st.selectbox("Choose Character 👤", list(characters[universe].keys()))

st.subheader(f"{character} from {universe}")
st.info(characters[universe][character])

# -----------------------------
# CHALLENGES (HIDDEN TITLES)
# -----------------------------
st.write("## ⚔️ Trials of the Multiverse")

# IMPORTANT: Titles are now intentionally vague
challenges = {
    "Pokemon": [
        ("Trial of Storms", "This creature stores electricity in its cheeks. What type is it?", "electric"),
        ("Trial of Elements", "Which element defeats flame in battle logic?", "water"),
        ("Trial of Evolution", "This creature has multiple final forms. How many main evolutions exist for it?", "8")
    ],
    "Wings of Fire": [
        ("Trial of Loyalty", "This dragon belongs to the tribe known for mud and strength.", "mudwing"),
        ("Trial of Rain", "Which tribe is known for rainforest camouflage and venom spit?", "rainwing"),
        ("Trial of Sands", "Which tribe survives in the desert under harsh sun?", "sandwing")
    ],
    "LEGO": [
        ("Trial of Flames", "Which element is controlled by the red ninja?", "fire"),
        ("Trial of Leadership", "Who is the green ninja destined to lead?", "lloyd"),
        ("Trial of Frost", "Which ninja is part machine and controls ice?", "zane")
    ],
    "Mario": [
        ("Trial of Shadows", "Who is the brother of the main red hero?", "luigi"),
        ("Trial of Courage", "This character is known for bravery despite fear.", "luigi"),
        ("Trial of Beasts", "What dinosaur-like companion travels with Mario?", "yoshi")
    ]
}

selected = challenges[universe]

# -----------------------------
# GAME LOOP
# -----------------------------
for i, (title, question, answer) in enumerate(selected):

    st.write("### 🔮 Unknown Trial")
    st.write(question)

    key = f"{universe}_{i}"

    if key not in st.session_state.done:

        user_answer = st.text_input("Your answer", key=key)

        if st.button("Submit", key=f"btn_{key}"):

            if user_answer.lower().strip() == answer:
                st.success("Correct! +25 XP earned ⚡")
                st.session_state.xp += 25
                st.session_state.done[key] = True

                st.session_state.history.append(
                    f"{character} conquered a hidden trial in {universe}"
                )

            else:
                st.error("Incorrect... the multiverse rejects your answer ❌")

    else:
        st.success("Trial already completed ✅")

# -----------------------------
# XP SYSTEM
# -----------------------------
st.write("## ⭐ Hero Progress")

st.metric("XP", st.session_state.xp)
st.progress((st.session_state.xp % 100) / 100)

# -----------------------------
# JOURNEY LOG
# -----------------------------
st.write("## 📜 Chronicle of Adventures")

if st.session_state.history:
    for h in reversed(st.session_state.history):
        st.write("•", h)
else:
    st.write("No trials conquered yet...")

# -----------------------------
# STATS
# -----------------------------
st.write("## 📊 Multiverse Status")

col1, col2 = st.columns(2)

with col1:
    st.metric("Universe", universe)

with col2:
    st.metric("Active Trials", len(selected))
