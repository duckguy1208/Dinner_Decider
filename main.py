import random

import streamlit as st

st.title("Dinner Generator")
st.header("Enter Your Choices For Dinner")

if "options" not in st.session_state:
    st.session_state.options = []


def add_option() -> None:
    new_option = st.session_state.option_input
    if not new_option.strip():
        st.warning("Please enter a non-empty option.")
        return

    st.session_state.options.append(new_option.strip())
    st.session_state.option_input = ""

option_text = st.text_input(
    "Enter a restaurant name or dish name:",
    key="option_input"
)



if st.button("Add Option", on_click=add_option):
    pass

if st.button("Generate Dinner"):
    if st.session_state.options:
        dinner_choice = random.choice(st.session_state.options)
        st.subheader(f"Tonight's dinner choice: {dinner_choice.title()}")
    else:
        st.warning("Please add some options before generating a dinner choice.")

st.divider()

st.write("### Current options")
if st.session_state.options:
    for option in st.session_state.options:
        st.write(option.title())
else:
    st.info("No options added yet. Add one before generating.")

if st.button("Clear Options"):
    st.session_state.options.clear()
    st.success("All options cleared.")
