import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Lumen AI", layout="wide", page_icon="🛡️")

# --- UI STYLING (CORRECTED) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div.stButton > button:first-child {
        background-color: #2e7bcf;
        color: white;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True) # FIXED: changed index to html

st.title("🛡️ Lumen: Tutor Mode")
st.write("Your personal engineering entrance exam coach.")

st.divider()

# Input area
topic = st.text_input("Enter a concept to master:", placeholder="e.g. Bernoulli's Principle")

if st.button("Explain to Me"):
    if topic:
        with st.spinner("Lumen is analyzing the concept..."):
            try:
                # Custom prompt tailored for JEE/MHT-CET
                prompt = (f"Explain the concept of {topic} for an 18-year-old student preparing for "
                          f"competitive exams like JEE and MHT-CET. Use clear bullet points, "
                          f"include the most important formulas, and provide one practical example.")
                
                response = model.generate_content(prompt)
                
                st.success(f"Concept: {topic}")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a topic first!")

st.sidebar.title("Lumen Settings")
st.sidebar.info("Tutor Mode: Active")
