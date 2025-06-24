import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json




# Where to store journal entries
DATA_FILE = "data/journal.json"

def save_entry(entry):
    # Create file if it doesn't exist
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    # Load existing data
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    # Append the new entry
    data.append(entry)

    # Save it back
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # Return empty list if file is empty or invalid
    else:
        return []


# Load the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Journal", layout="centered")
st.title("🧠 Gemini-Powered Journal Assistant")

date = st.date_input("Date: ")
mood = st.text_input("How's your mood today?")
journal = st.text_area("✍️ What's on your mind today?")

if st.button("Reflect with Gemini"):
    if not journal.strip():
        st.warning("Please write something first!")
    else:
        with st.spinner("Gemini is thinking..."):
            try:
                prompt = f"""You are a compassionate mental health assistant.
                Read this journal entry and reflect on it gently, supportively, an>

                Entry:
                {journal}
                """
                response = model.generate_content(prompt)
                st.success("Here's your reflection 💬")
                st.markdown(f"> {response.text}")
            except Exception as e:
                st.error(f"Something went wrong:\n\n{str(e)}")

#saving the reflection

    entry = {
        "date": str(date),
        "mood": mood,
        "entry": journal,
        "reflection": response.text
    }
    save_entry(entry)
    st.success("Journal entry saved!")




#sidebar of previous logs

with st.expander("📚 View Past Journal Entries"):
    entries = load_entries()
    if not entries:
        st.info("No past entries yet.")
    else:
        for e in reversed(entries):
            st.markdown(f"### 📅 {e['date']} — Mood: *{e['mood']}*")
            st.markdown(f"**Journal:** {e['entry']}")
            st.markdown(f"**Reflection:** {e['reflection']}")
            st.markdown("---")

