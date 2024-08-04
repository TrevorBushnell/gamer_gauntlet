import streamlit as st
import random
import json
import base64

# Read the contestant's challenges
with open ('frobuddy_challenges.json', 'r') as f:
    challenges_list = json.load(f)

random.shuffle(challenges_list)

if 'challenges' not in st.session_state:
    st.session_state.challenges = challenges_list

if 'curr_challenge' not in st.session_state:
    st.session_state.curr_challenge = {"challenge":"START", "stars":""}

# Raed in the GIF of me for keeping track of points
with open("./trevvy.gif", "rb") as g:
    contents = g.read()
    data_url = base64.b64encode(contents).decode("utf-8")

if st.button("NEW CHALLENGE"):
    st.session_state.curr_challenge = st.session_state.challenges.pop()

st.markdown(f"### {st.session_state.curr_challenge['challenge']} ({st.session_state.curr_challenge['stars']})")

cols = st.columns(10)

for i, col in enumerate(cols):
    with col:
        checkbox = st.checkbox(f" ", key=f"box_{i}")

        if checkbox:
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="star!">', unsafe_allow_html=True)
