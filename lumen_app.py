import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 
genai.configure(api_key=API_KEY)

# UPDATED: Using the official stable model name
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Lumen AI", layout="wide", page_icon="🛡️")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background-color: #2e7bcf;
        color: white;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Lumen: Tutor Mode")
st.write("Your personal engineering entrance exam coach.")

st.divider()

topic = st.text_input("Enter a concept to master:", placeholder="e.g. Rotational Dynamics")

if st.button("Explain to Me"):
    if topic:
        with st.spinner("Lumen is analyzing..."):
            try:
                # Custom prompt for your JEE/MHT-CET prep
                prompt = (f"Explain {topic} for a JEE/MHT-CET student. "
                          f"Include: 1. Core Concept, 2. Key Formulas, 3. One solved-style example.")
                
                response = model.generate_content(prompt)
                
                st.success(f"Concept: {topic}")
                st.markdown(response.text)
                
            except Exception as e:
                # If flash-latest fails, try the generic flash name as backup
                try:
                    backup_model = genai.GenerativeModel('gemini-1.5-flash')
                    response = backup_model.generate_content(topic)
                    st.markdown(response.text)
                except:
                    st.error(f"AI Connection Error. Please check your API key status.")
    else:
        st.warning("Please enter a topic first!")

st.sidebar.info("Lumen Tutor Mode is Live")
