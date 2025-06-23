import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Journal", layout="centered")
st.title("🧠 Gemini-Powered Journal Assistant")

journal = st.text_area("✍️ What's on your mind today?")

if st.button("Reflect with Gemini"):
    if not journal.strip():
        st.warning("Please write something first!")
    else:
        with st.spinner("Gemini is thinking..."):
            try:
                prompt = f"""You are a compassionate mental health assistant. 
                Read this journal entry and reflect on it gently, supportively, and kindly.

                Entry:
                {journal}
                """
                response = model.generate_content(prompt)
                st.success("Here's your reflection 💬")
                st.markdown(f"> {response.text}")
            except Exception as e:
                st.error(f"Something went wrong:\n\n{str(e)}")
