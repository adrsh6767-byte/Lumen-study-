import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
# Your unique API Key is now integrated
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Lumen AI", layout="wide", page_icon="🛡️")

# Custom CSS to make it look clean on mobile
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7bcf;
        color: white;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("🛡️ Lumen: Tutor Mode")
st.write("Your personal engineering entrance exam coach.")

st.divider()

# Input area
topic = st.text_input("Enter a concept to master:", placeholder="e.g. Capacitor in Series")

if st.button("Explain to Me"):
    if topic:
        with st.spinner("Lumen is analyzing the concept..."):
            try:
                # Custom prompt tailored for your prep level
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
st.sidebar.write("Currently using Gemini 1.5 Flash for high-speed explanations.")
