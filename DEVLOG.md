# 🧠 Dev Log – Mental Health Journal AI

This file tracks daily progress, learnings, and key milestones while building the AI-powered journaling dashboard using Streamlit and Gemini 1.5 Flash.

---

## ✅ Day 1

- Set up the project directory and initialized a Git repository
- Created and activated a Python virtual environment
- Installed and tested the Streamlit framework
- Built the initial journaling UI with:
  - Date input
  - Mood selector (dropdown)
  - Text area for journal entry
- Learned the difference between `st.write()` and `st.markdown()`
- Understood how Streamlit renders components top-to-bottom

---

## ✅ Day 2

- Attempted OpenAI integration, but encountered quota limits and deprecation issues
- Switched to Google’s Gemini 1.5 Flash model using the `google.generativeai` SDK
- Successfully authenticated and made the first AI call
- Built prompt templates for reflective journaling
- Gemini now returns personalized responses based on user input
- Gained deeper understanding of how to handle:
  - API key management
  - Python environment errors
  - Gemini’s input-output formatting

---

## 🔜 Day 3 Goals

- Save each entry + AI reflection to a local file (e.g., JSON or CSV)
- Begin building a simple data visualization of mood trends over time
- Explore ways to add journaling security (e.g., optional password gate)

---

## Notes

This is a continuous build-measure-learn project. The goal isn’t just completion — but improving code quality, design thinking, and API mastery with every iteration.
