import streamlit as st

st.set_page_config(page_title="Mental Health Journal", layout="centered")

st.title("Metal Health Dashboard")
mood= st.selectbox("Select your mood: ", ["Happy","OKay","Sad","Depressed","Freaky"])
entry= st.text_area("Write about your day: ")

if st.button("Submit"):
	st.success("Thanks for sharing. Here is waht we got:")
	st.write(f"Mood: {mood}")
	st.markdown(f"Jornal Entry: {entry}")
